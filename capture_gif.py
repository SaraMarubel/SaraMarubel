import os
import io
from playwright.sync_api import sync_playwright
from PIL import Image

OUT_DIR = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(OUT_DIR, exist_ok=True)

VIEWPORT = {"width": 1000, "height": 640}


def save_gif(frames, out_path, duration_ms=350):
    imgs = [Image.open(io.BytesIO(f)).convert("P", palette=Image.ADAPTIVE, colors=128) for f in frames]
    imgs[0].save(
        out_path,
        save_all=True,
        append_images=imgs[1:],
        duration=duration_ms,
        loop=0,
        optimize=True,
    )
    print(f"  saved {out_path} ({len(imgs)} frames, {os.path.getsize(out_path)/1024:.0f} KB)")


def capture_msft_trader(page):
    """Seed near-crossover state, let ticks run, force a visible auto BUY then SELL
    via the app's own trade-execution functions (autoBuy/autoSell) so the GIF shows
    a real round-trip trade, chart markers, and blotter update."""
    page.goto("https://saramarubel.github.io/msft-algo-trader/", wait_until="networkidle")
    page.wait_for_timeout(1500)

    frames = []
    for _ in range(6):
        frames.append(page.screenshot())
        page.wait_for_timeout(700)

    page.evaluate("""() => {
        const closes = [];
        for (let i = 0; i < 25; i++) closes.push(TICKERS[0].price - 1 + i * 0.04);
        state.msftCloses = closes;
        const f = sma(closes, SMA_FAST), s = sma(closes, SMA_SLOW);
        state.prevSmaFast = s - 0.02; state.prevSmaSlow = s;
        autoBuy(TICKERS[0].price, 'SMA(9) crossed above SMA(21) — bullish signal');
    }""")

    for _ in range(6):
        frames.append(page.screenshot())
        page.wait_for_timeout(700)

    page.evaluate("""() => {
        autoSell(TICKERS[0].price, 'Take-profit triggered (+5.00%)');
    }""")

    for _ in range(6):
        frames.append(page.screenshot())
        page.wait_for_timeout(700)

    return frames


def capture_scroll(page, url, scroll_steps=14, step_px=140, settle_ms=350):
    page.goto(url, wait_until="networkidle")
    page.wait_for_timeout(1000)
    frames = [page.screenshot()]
    for _ in range(scroll_steps):
        page.mouse.wheel(0, step_px)
        page.wait_for_timeout(settle_ms)
        frames.append(page.screenshot())
    # hold on last frame, then scroll back to top for a clean loop
    frames.append(page.screenshot())
    page.evaluate("window.scrollTo({top: 0, behavior: 'smooth'})")
    page.wait_for_timeout(900)
    frames.append(page.screenshot())
    return frames


def capture_pizza(page):
    page.goto("https://saramarubel.github.io/Customer-Interface-system1/", wait_until="networkidle")
    page.wait_for_timeout(800)
    frames = [page.screenshot()]

    box = page.get_by_placeholder("e.g. SE1 6NP").first
    box.click()
    for ch in "SE1 6NP":
        box.type(ch, delay=90)
        frames.append(page.screenshot())

    page.get_by_role("button", name="Find").first.click()
    for _ in range(5):
        page.wait_for_timeout(400)
        frames.append(page.screenshot())

    return frames


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport=VIEWPORT)

    print("Capturing msft-algo-trader...")
    save_gif(capture_msft_trader(page), os.path.join(OUT_DIR, "msft-algo-trader.gif"))

    print("Capturing equity-research-report...")
    save_gif(
        capture_scroll(page, "https://saramarubel.github.io/equity-research-report/"),
        os.path.join(OUT_DIR, "equity-research-report.gif"),
        duration_ms=280,
    )

    print("Capturing ETF-basket-analysis...")
    save_gif(
        capture_scroll(page, "https://saramarubel.github.io/ETF-basket-analysis/"),
        os.path.join(OUT_DIR, "ETF-basket-analysis.gif"),
        duration_ms=280,
    )

    print("Capturing Customer-Interface-system1...")
    save_gif(capture_pizza(page), os.path.join(OUT_DIR, "Customer-Interface-system1.gif"), duration_ms=250)

    browser.close()
