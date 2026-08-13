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

</div>

## Adding a new series

1. Create a new file in `docs/portfolio/`, e.g. `street.md`
2. Add web-sized exports to `docs/assets/images/street/`
3. Register the page under `nav:` in `mkdocs.yml`
4. Add a card above so it's reachable from this page

!!! warning "Export sizes"

    Keep images under ~500 KB each. GitHub Pages has a **1 GB** repo soft limit
    and a **100 GB/month** bandwidth limit — full-resolution exports will chew
    through both. 2000px on the long edge at quality 80 is plenty for web.
