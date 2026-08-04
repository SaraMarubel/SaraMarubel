import os
from playwright.sync_api import sync_playwright
from capture_gif import save_gif, OUT_DIR, VIEWPORT

URL = "https://saramarubel.github.io/msft-algo-trader/"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport=VIEWPORT)
    page.goto(URL, wait_until="networkidle")
    page.wait_for_timeout(1500)

    frames = []
    # just the live dashboard: backfilled candles, BUY/SELL markers, and
    # the blotter ticking as the algorithm keeps trading in real time
    for _ in range(22):
        frames.append(page.screenshot())
        page.wait_for_timeout(600)

    browser.close()
    save_gif(frames, os.path.join(OUT_DIR, "msft-algo-trader.gif"), duration_ms=320)
