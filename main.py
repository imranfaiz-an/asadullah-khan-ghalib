from divan_e_ghalib.scrape import scrape_ghazal
import json
import time
from pathlib import Path


def build_json():
    out = Path("ghazals") / "divan.json"
    out.parent.mkdir(parents=True, exist_ok=True)

    all_ghazals = {}
    for n in range(1, 235):
        try:
            all_ghazals.update(scrape_ghazal(n))
        except Exception as e:
            print(n, e)
        time.sleep(1)

    with open(out, "w", encoding="utf-8") as f:
        json.dump(all_ghazals, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    build_json()
