#!/usr/bin/env python3
"""Build a photo gallery for this site from a folder of Lightroom exports.

Does three things in one pass:

1. Resizes exports to the web budget documented on the portfolio page
   (2000px long edge, under ~500 KB), preserving the ICC profile and EXIF so
   colour management and copyright survive the re-encode.
2. Reads each file's IPTC ``Title`` and uses it as the image's alt text. The
   glightbox ``auto_caption`` option turns alt text into the lightbox caption,
   so captions stay tied to what Lightroom holds rather than to anything
   maintained by hand here.
3. Rewrites the ``<div class="gallery">`` block on a target page in place,
   leaving the heading and surrounding prose untouched.

Requires ``exiftool`` (``brew install exiftool``) and Pillow. Pillow is
deliberately NOT in requirements.txt — that file pins what CI needs to build
the site, and this script only ever runs locally.

    pip install Pillow

Examples
--------
Rebuild Postcards after a re-export (frame 35 has no IPTC Title, so its
caption has to be supplied explicitly)::

    python3 tools/build_gallery.py postcards \\
        --source ~/Desktop/2_Web \\
        --page docs/portfolio/postcards.md \\
        --prefix postcard \\
        --untitled-caption "Self Reflection with a Nikon SLR"

Fill in the Landscapes series, which works the same way::

    python3 tools/build_gallery.py landscapes \\
        --source ~/Desktop/landscapes-export \\
        --page docs/portfolio/landscapes.md

Always try ``--dry-run`` first: it reports every resize and the caption each
image would get, without writing an image or touching the page.

Ordering
--------
``--order auto`` (the default) uses the leading number in the filename when
every source has one — an export named ``12--Postcard.JPG`` sorts to position
12. This matters because ``10`` sorts before ``2`` lexically, so filename order
is not sequence order. Without leading numbers it falls back to IPTC Title,
alphabetically. Output files are named ``<prefix>-NN.jpg``, zero-padded, so
filesystem, URL and display order agree. ``--prefix`` defaults to the series
name; Postcards overrides it to the singular ``postcard`` because the files are
already published under those names and renaming them would break links.

Note that renumbering is positional: adding a photo to the middle of a series
renames everything after it. That is churn in git, but it keeps the ordering
guarantee, and old files are removed rather than left orphaned.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import shutil
import subprocess
import sys

try:
    from PIL import Image
except ImportError:  # pragma: no cover - dependency guidance
    sys.exit("Pillow is required: pip install Pillow")

REPO = pathlib.Path(__file__).resolve().parent.parent

# sips ships with macOS but silently ignores its own quality flag — a 17 MB
# folder came back out at 25 MB. Pillow is used instead for that reason.
DEFAULT_LONG_EDGE = 2000
DEFAULT_BUDGET_KB = 500
FALLBACK_LONG_EDGE = 1600
QUALITY_LADDER = (85, 80, 75, 70, 65)
FALLBACK_LADDER = (80, 75, 70, 65, 60)

GALLERY_RE = re.compile(r'<div class="gallery" markdown>.*?</div>', re.S)
SOURCE_SUFFIXES = {".jpg", ".jpeg", ".JPG", ".JPEG"}


def read_titles(source: pathlib.Path) -> dict[str, str]:
    """Map filename -> IPTC Title, for files that have one."""
    try:
        proc = subprocess.run(
            ["exiftool", "-q", "-q", "-T", "-FileName", "-Title", "."],
            capture_output=True, text=True, cwd=source, check=True,
        )
    except FileNotFoundError:
        sys.exit("exiftool not found. Install it with: brew install exiftool")
    titles = {}
    for line in proc.stdout.strip().splitlines():
        if "\t" not in line:
            continue
        name, title = line.split("\t", 1)
        if title != "-":
            titles[name] = title
    return titles


def order_sources(sources: list[pathlib.Path], titles: dict[str, str],
                  mode: str) -> list[pathlib.Path]:
    leading = {p: re.match(r"(\d+)", p.name) for p in sources}
    if mode == "auto":
        mode = "numeric" if all(leading.values()) else "title"

    if mode == "numeric":
        missing = [p.name for p in sources if not leading[p]]
        if missing:
            sys.exit("--order numeric needs a leading number on every file; "
                     f"missing on: {', '.join(sorted(missing)[:5])}")
        return sorted(sources, key=lambda p: int(leading[p].group(1)))
    if mode == "title":
        return sorted(sources, key=lambda p: titles.get(p.name, p.name).lower())
    return sorted(sources, key=lambda p: p.name.lower())


def encode(src: pathlib.Path, dest: pathlib.Path, long_edge: int,
           budget: int) -> tuple[int, int, tuple[int, int]]:
    """Write a web-sized copy. Returns (bytes, quality, dimensions)."""
    def attempt(edge: int, ladder: tuple[int, ...]):
        with Image.open(src) as im:
            icc, exif = im.info.get("icc_profile"), im.info.get("exif")
            im.thumbnail((edge, edge), Image.LANCZOS)
            for quality in ladder:
                im.save(dest, "JPEG", quality=quality, optimize=True,
                        progressive=True, icc_profile=icc, exif=exif)
                if dest.stat().st_size <= budget:
                    break
            return dest.stat().st_size, quality, im.size

    size, quality, dims = attempt(long_edge, QUALITY_LADDER)
    if size > budget:
        # Heavy film grain is high-entropy and resists JPEG compression. Drop
        # the long edge rather than crushing quality into mush.
        size, quality, dims = attempt(FALLBACK_LONG_EDGE, FALLBACK_LADDER)
    return size, quality, dims


def render_gallery(entries: list[tuple[str, str]], series: str) -> str:
    lines = ['<div class="gallery" markdown>', ""]
    for slug, caption in entries:
        escaped = caption.replace("[", "\\[").replace("]", "\\]")
        lines.append(
            f"![{escaped}](../assets/images/{series}/{slug}){{ loading=lazy }}")
        lines.append("")
    lines.append("</div>")
    return "\n".join(lines)


def splice(page: pathlib.Path, gallery: str, section: str | None) -> None:
    text = page.read_text()
    if section:
        heading = re.search(rf"^##+\s+{re.escape(section)}\s*$", text, re.M)
        if not heading:
            sys.exit(f"no heading '{section}' in {page}")

        tail = text[heading.end():]
        match = GALLERY_RE.search(tail)
        if not match:
            sys.exit(f"no gallery block under '{section}' in {page}")
        start = heading.end() + match.start()
        end = heading.end() + match.end()
        page.write_text(text[:start] + gallery + text[end:])
        return

    blocks = GALLERY_RE.findall(text)
    if len(blocks) != 1:
        sys.exit(f"expected exactly one gallery block in {page}, found "
                 f"{len(blocks)}. Pass --section to disambiguate.")
    page.write_text(GALLERY_RE.sub(lambda _: gallery, text))


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("series", help="series name, e.g. postcards. Sets the "
                                       "image folder and filename prefix.")
    parser.add_argument("--source", required=True, type=pathlib.Path,
                        help="folder of Lightroom exports")
    parser.add_argument("--page", required=True, type=pathlib.Path,
                        help="markdown page holding the gallery block")
    parser.add_argument("--section", default=None,
                        help="heading whose gallery to replace; omit if the "
                             "page has exactly one gallery")
    parser.add_argument("--prefix", default=None,
                        help="filename prefix for output images; defaults to "
                             "the series name. Postcards uses the singular "
                             "'postcard' because the files are already live "
                             "under those names.")
    parser.add_argument("--order", default="auto",
                        choices=["auto", "numeric", "title", "filename"])
    parser.add_argument("--untitled-caption", default=None,
                        help="caption for files with no IPTC Title. Without "
                             "this the run aborts and lists them.")
    parser.add_argument("--long-edge", type=int, default=DEFAULT_LONG_EDGE)
    parser.add_argument("--budget-kb", type=int, default=DEFAULT_BUDGET_KB)
    parser.add_argument("--dry-run", action="store_true",
                        help="report what would happen, write nothing")
    args = parser.parse_args()

    source = args.source.expanduser().resolve()
    if not source.is_dir():
        sys.exit(f"source folder not found: {source}")
    page = (args.page if args.page.is_absolute() else REPO / args.page).resolve()
    if not page.is_file():
        sys.exit(f"page not found: {page}")

    sources = [p for p in source.iterdir() if p.suffix in SOURCE_SUFFIXES]
    if not sources:
        sys.exit(f"no JPEGs in {source}")

    titles = read_titles(source)
    untitled = [p.name for p in sources if p.name not in titles]
    if untitled and args.untitled_caption is None:
        sys.exit(
            f"{len(untitled)} file(s) have no IPTC Title, so they have no "
            "caption:\n  " + "\n  ".join(sorted(untitled)) +
            "\n\nSet a Title in Lightroom and re-export, or pass "
            "--untitled-caption to supply one for all of them."
        )

    prefix = args.prefix or args.series
    ordered = order_sources(sources, titles, args.order)
    budget = args.budget_kb * 1024
    dest_dir = REPO / "docs/assets/images" / args.series

    entries: list[tuple[str, str]] = []
    planned = {f"{prefix}-{n:02d}.jpg" for n in range(1, len(ordered) + 1)}

    if not args.dry_run:
        dest_dir.mkdir(parents=True, exist_ok=True)
        # Remove only this series' own numbered files, so anything else living
        # in the folder is left alone rather than silently deleted.
        for old in dest_dir.glob(f"{prefix}-*.jpg"):
            if old.name not in planned:
                old.unlink()

    total = 0
    over: list[str] = []
    for n, src in enumerate(ordered, start=1):
        slug = f"{prefix}-{n:02d}.jpg"
        caption = titles.get(src.name, args.untitled_caption)
        if args.dry_run:
            with Image.open(src) as im:
                dims = im.size
            print(f"  {slug}  <- {src.name:24s} {dims[0]}x{dims[1]}  {caption}")
        else:
            size, quality, dims = encode(src, dest_dir / slug, args.long_edge,
                                         budget)
            total += size
            if size > budget:
                over.append(slug)
            print(f"  {slug}  <- {src.name:24s} {size/1024:5.0f} KB  q{quality}"
                  f"  {dims[0]}x{dims[1]}  {caption}")
        entries.append((slug, caption))

    gallery = render_gallery(entries, args.series)

    if args.dry_run:
        print(f"\nDry run: {len(entries)} images, nothing written.")
        print(f"Would rewrite the gallery block in {page.relative_to(REPO)}"
              + (f" under '{args.section}'." if args.section else "."))
        strays = [p.name for p in dest_dir.glob("*.jpg")
                  if p.name not in planned] if dest_dir.exists() else []
        if strays:
            print(f"Would delete {len(strays)} superseded file(s): "
                  f"{', '.join(sorted(strays)[:5])}")
        return

    splice(page, gallery, args.section)
    print(f"\n{len(entries)} images -> {total/1024/1024:.1f} MB in "
          f"{dest_dir.relative_to(REPO)}")
    if over:
        print(f"over the {args.budget_kb} KB budget (grain resists JPEG): "
              f"{', '.join(over)}")
    print(f"rewrote gallery in {page.relative_to(REPO)}")
    print("\nNext: .venv/bin/mkdocs build --strict, then commit and push.")


if __name__ == "__main__":
    main()
