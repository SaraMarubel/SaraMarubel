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

    # dashboard running, backfilled chart + market clock visible
    for _ in range(5):
        frames.append(page.screenshot())
        page.wait_for_timeout(500)

    # open Strategy Settings modal
    page.locator("#settingsBtn").click()
    page.wait_for_timeout(400)
    frames.append(page.screenshot())
    frames.append(page.screenshot())
    page.locator("#settingsClose").click()
    page.wait_for_timeout(300)

    # switch chart to AAPL and enable its algo
    page.get_by_text("Apple Inc.").click()
    page.wait_for_timeout(500)
    frames.append(page.screenshot())
    page.locator('.algo-toggle[data-symbol="AAPL"]').click()
    page.wait_for_timeout(600)
    frames.append(page.screenshot())
    frames.append(page.screenshot())

    # back to MSFT for the close-out frames
    page.get_by_text("Microsoft Corp.").first.click()
    page.wait_for_timeout(500)
    for _ in range(6):
        frames.append(page.screenshot())
        page.wait_for_timeout(500)

    browser.close()
    save_gif(frames, os.path.join(OUT_DIR, "msft-algo-trader.gif"), duration_ms=320)
