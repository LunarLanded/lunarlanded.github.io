# C Siegel Photography — site source

Static site built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/),
deployed to GitHub Pages by GitHub Actions.

## Local development

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

Open <http://127.0.0.1:8000>. The server live-reloads on save.

## First-time setup checklist

- [ ] Replace `<handle>` (Instagram) in `mkdocs.yml` and `docs/about/contact.md`
- [ ] Add the `docs` CNAME DNS record (see Domain below)
- [ ] Confirm `hello@csiegel.photography` is a real inbox (it's used in three places)
- [ ] Drop a real `docs/assets/images/favicon.png`
- [ ] Replace the placeholder gallery images
- [ ] Write the actual copy in `docs/about/index.md` and `docs/plugin/index.md`
- [ ] Have the licence and refund terms reviewed before publishing

## Push it to GitHub

This folder is already a git repo with `origin` set to
`https://github.com/LunarLanded/lunarlanded.github.io`. Everything is staged but
not committed, so:

```bash
cd ~/Claude/GitPage
git commit -m "Initial site"
git branch -M main
git push -u origin main
```

If the remote already has commits, `git pull --rebase origin main` first.

The `ci` workflow runs on push, builds with `--strict`, and pushes the built HTML
to a `gh-pages` branch. **Source stays on `main`; only the output goes to
`gh-pages`.** Don't hand-edit `gh-pages` — it's regenerated every deploy.

Then in **Settings → Pages**, set the source to **Deploy from a branch →
`gh-pages` / `(root)`**. The branch only exists after the first successful
workflow run, so if it's not in the dropdown yet, wait for the Action to finish.

### A note on this being the user-site repo

`lunarlanded.github.io` is a *user site*, which serves at the root of your Pages
domain rather than under a subpath. Two consequences:

- Once you set the custom domain below, **every** project repo under
  `LunarLanded` with Pages enabled will also be served from it, at
  `docs.csiegel.photography/<repo-name>/`. Harmless, just slightly odd naming.
- User sites can publish from any branch, `gh-pages` included, so the workflow
  here works as-is.

## Domain — docs.csiegel.photography

The main site is on Adobe, so a `/docs` subpath isn't available: one domain
can't point at two hosts. This is set up for a **subdomain** instead, which is
the cleaner arrangement anyway — it's completely independent of the main site,
so nothing here breaks when you move off Adobe.

### DNS

At whoever holds DNS for `csiegel.photography`, add one record:

| Type | Host / Name | Value |
| ---- | ----------- | ----- |
| `CNAME` | `docs` | `lunarlanded.github.io` |

That's it. This record only affects the `docs.` subdomain — your existing Adobe
records for the apex and `www` are untouched, and the main site keeps working
throughout.

Some DNS panels want a trailing dot (`lunarlanded.github.io.`); some add it for
you. Both are correct.

### GitHub

1. Push this repo (see above) and let the `ci` workflow finish.
2. **Settings → Pages** → source = **Deploy from a branch** → `gh-pages` / `(root)`.
3. **Settings → Pages → Custom domain** → `docs.csiegel.photography` → Save.
4. Wait for the certificate to issue, then tick **Enforce HTTPS**. Usually
   minutes; occasionally up to 24 hours.

### Why `docs/CNAME` exists

`gh-deploy --force` rebuilds the `gh-pages` branch from scratch on every deploy.
A `CNAME` file that GitHub's UI wrote directly to that branch would be deleted
on the next push, and your custom domain would silently unset itself.

Keeping `CNAME` in `docs/` means MkDocs copies it into the build output every
time, so it survives. Don't move it.

### When you move the main site off Adobe

Nothing breaks — `docs.csiegel.photography` keeps serving throughout, because the
`docs` DNS record is independent of the apex.

But note the one bit of rework you've deferred: this site occupies the user-site
repo, which is the only repo that can serve the *apex* `csiegel.photography`. So
when you're ready to host the main photography site on GitHub Pages too, you'll
need to:

1. Create a project repo (e.g. `LunarLanded/docs`) and move this site into it,
   keeping `docs/CNAME` as-is.
2. Point the user-site repo at the main site instead, and set its custom domain
   to `csiegel.photography`.

It's a repo move, not a rewrite — the MkDocs config and content carry over
unchanged. Worth knowing it's coming rather than discovering it mid-migration.

## Adding a page

1. Create the `.md` file under `docs/`
2. Add it to `nav:` in `mkdocs.yml` — the build runs with `--strict`, so an
   unlisted file or a broken link will fail CI rather than deploy quietly

## Layout

```
.
├── mkdocs.yml              # all site config
├── requirements.txt        # pinned deps, used by CI and locally
├── .github/workflows/ci.yml
├── overrides/main.html     # theme template overrides
└── docs/
    ├── index.md
    ├── CNAME               # docs.csiegel.photography
    ├── portfolio/
    ├── plugin/
    ├── about/
    └── assets/
        ├── images/
        └── stylesheets/extra.css
```
