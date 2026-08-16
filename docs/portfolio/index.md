# Portfolio

Work grouped into series. Click any image to open it full-size.

<div class="grid cards" markdown>

-   __Landscapes__

    ---

    Wide country, long exposures, and a lot of early mornings.

    [:octicons-arrow-right-24: View series](landscapes.md)

-   __Portraits__

    ---

    Available light, mostly. People I know and people I met once.

    [:octicons-arrow-right-24: View series](portraits.md)

-   __Postcards__

    ---

    One frame per place, thirty-five in all. Nine of them are Nicaragua.

    [:octicons-arrow-right-24: View series](postcards.md)

</div>

## Adding a new series

1. Create a new file in `docs/portfolio/`, e.g. `street.md`, with an empty
   `<div class="gallery" markdown>` / `</div>` block where the photos go
2. Run `tools/build_gallery.py` to resize the exports into
   `docs/assets/images/street/` and fill in that block:

    ```bash
    python3 tools/build_gallery.py street \
        --source ~/Desktop/street-export \
        --page docs/portfolio/street.md --dry-run
    ```

    Drop `--dry-run` once the listing looks right. Captions come from each
    file's IPTC `Title`, so set those in Lightroom before exporting.

3. Register the page under `nav:` in `mkdocs.yml`
4. Add a card above so it's reachable from this page

!!! warning "Export sizes"

    Keep images under ~500 KB each. GitHub Pages has a **1 GB** repo soft limit
    and a **100 GB/month** bandwidth limit — full-resolution exports will chew
    through both. 2000px on the long edge at quality 80 is plenty for web.
