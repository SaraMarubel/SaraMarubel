import os
from playwright.sync_api import sync_playwright
from capture_gif import save_gif, OUT_DIR, VIEWPORT

URL = "https://saramarubel.github.io/msft-algo-trader/"


def click_ticker(page, symbol):
    page.locator(f'.ticker-card[data-symbol="{symbol}"] .name').click()
    page.evaluate("window.scrollTo(0, 0)")


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport=VIEWPORT)
    page.goto(URL, wait_until="networkidle")
    page.wait_for_timeout(1200)

    frames = []

    # MSFT: backfilled candles, BUY/SELL markers, blotter ticking
    for _ in range(14):
        frames.append(page.screenshot())
        page.wait_for_timeout(450)

    # then show the other tracked stocks by switching the chart to each
    for symbol in ["AAPL", "GOOGL", "AMZN"]:
        click_ticker(page, symbol)
        page.wait_for_timeout(350)
        frames.append(page.screenshot())
        page.wait_for_timeout(350)
        frames.append(page.screenshot())

    browser.close()
    save_gif(frames, os.path.join(OUT_DIR, "msft-algo-trader.gif"), duration_ms=180)
