import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import lxml.html 
    import httpx
    import cssselect
    from playwright.async_api import async_playwright
    from lxml import html

    return async_playwright, html, httpx, lxml


@app.cell
def _(httpx, lxml):
    resp = httpx.get("https://franpritchett.com/00ghalib/001/index_001.html")
    root = lxml.html.fromstring(resp.text)
    return


@app.cell
async def _(async_playwright, html):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://franpritchett.com/00ghalib/001/index_001.html")
        await page.wait_for_selector("select")
        await page.select_option("select", "نستعلیق")
        tree = html.fromstring(await page.content())
        await browser.close()

    verses = []
    for entry in tree.cssselect("div.verse-entry"):
        num = entry.cssselect("h3.verse-number a")[0].text
        lines = [t.strip() for t in entry.cssselect("p.verse-text")[0].itertext() if t.strip()]
        print(num, *lines, "", sep="\n")
    return


if __name__ == "__main__":
    app.run()
