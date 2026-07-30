import os
from playwright.sync_api import sync_playwright

TARGETS = [
    ("msft-algo-trader", "https://saramarubel.github.io/msft-algo-trader/", 5000),
    ("equity-research-report", "https://saramarubel.github.io/equity-research-report/", 2000),
    ("ETF-basket-analysis", "https://saramarubel.github.io/ETF-basket-analysis/", 2000),
    ("Customer-Interface-system1", "https://saramarubel.github.io/Customer-Interface-system1/", 2000),
]

OUT_DIR = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(OUT_DIR, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 800})
    for name, url, wait_ms in TARGETS:
        print(f"Capturing {name} -> {url}")
        page.goto(url, wait_until="networkidle", timeout=30000)
        page.wait_for_timeout(wait_ms)
        out_path = os.path.join(OUT_DIR, f"{name}.png")
        page.screenshot(path=out_path)
        print(f"  saved {out_path}")
    browser.close()
