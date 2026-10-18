from lxml import html
import cssselect
from playwright.sync_api import sync_playwright
from collections import defaultdict


base_url = "https://franpritchett.com/00ghalib"
additonal_url = "/001/index_001.html"


def construct_ghazal_url(n: int) -> str:
    ghazal_number = str(n).zfill(3)
    return base_url + "/" + ghazal_number + "/index_" + ghazal_number + ".html"


def scrape_ghazal(n):
    url = construct_ghazal_url(n)
    ghazal_dict = defaultdict(list)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector("select")
        page.select_option("select", "نستعلیق")
        tree = html.fromstring(page.content())
        browser.close()

    for entry in tree.cssselect("div.verse-entry"):
        num = entry.cssselect("h3.verse-number a")[0].text
        lines = [
            t.strip()
            for t in entry.cssselect("p.verse-text")[0].itertext()
            if t.strip()
        ]
        ghazal_dict[n].append({num: lines})

    return ghazal_dict
