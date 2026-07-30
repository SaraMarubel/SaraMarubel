import os
from playwright.sync_api import sync_playwright
from capture_gif import save_gif, OUT_DIR, VIEWPORT

URL = "https://saramarubel.github.io/starship-mars-transit/"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport=VIEWPORT)
    page.goto(URL, wait_until="networkidle")
    page.wait_for_timeout(1200)

    # speed up the mission clock via the real UI slider so stage progress
    # and camera parallax are visible within a short clip
    page.evaluate("""() => {
        const slider = document.getElementById('timeScale');
        slider.value = '3.5';
        slider.dispatchEvent(new Event('input', { bubbles: true }));
    }""")

    frames = []
    for _ in range(24):
        frames.append(page.screenshot())
        page.wait_for_timeout(500)

    browser.close()
    save_gif(frames, os.path.join(OUT_DIR, "starship-mars-transit.gif"), duration_ms=280)
