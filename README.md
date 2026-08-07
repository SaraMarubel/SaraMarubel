<h1 align="center">Sarah Beltran </h1>
<p align="center"><i>Physics student and AI Domain researcher, publishing projects undertaken in both my Finance and Astrophysics sectors of work.</i></p>

<br>

##  Finance Projects

### [Algo Trading Engine](https://github.com/SaraMarubel/algo-trading-engine)
A systematic long-only momentum strategy: SMA(9/21) crossover gated by a 50-period trend filter and an RSI(14) regime filter, with layered risk management (hard stop-loss, trailing stop, take-profit ceiling, re-entry cooldown) and fixed-fractional position sizing, trading a 6-name tech universe from market open against a live NYSE clock. Every parameter is tunable and persists client-side per ticker; large manual orders route through TWAP-sliced execution to reduce market impact, and a performance panel reports win rate, realized P&L, and trade-level attribution on a 3-hour cadence.

[<img src="assets/algo-trading-engine.gif" width="100%" alt="Algo Trading Engine live preview">](https://saramarubel.github.io/algo-trading-engine/)
<p><a href="https://saramarubel.github.io/algo-trading-engine/">🔗 Live demo</a></p>

### [LIVE Updating Equity Research Report: TSMC](https://github.com/SaraMarubel/equity-research-report)
An equity research report on TSMC (NYSE: TSM) structured the way a sell-side or quant research desk would actually cover it: business model and structural analysis (foundry economics, process-node roadmap, supply-chain dependencies), a live peer-comparison table benchmarking TSMC against Intel, Samsung Electronics, GlobalFoundries, UMC, and ASML on valuation multiples and margins, and a quantitative risk profile computing beta against both the S&P 500 and the SOXX semiconductor index, annualized volatility, Sharpe ratio, max drawdown, and cross-asset return correlation directly from price history, plus the geopolitical, regulatory, and environmental risk sections most retail-style dashboards skip entirely. Live market, valuation, and peer data is pulled through the Yahoo Finance API via the `yfinance` Python library, with a topic-grouped live news feed from the NewsAPI.org REST API; both are refreshed every four hours by a cron-scheduled GitHub Actions workflow that commits fresh JSON to the repo, and rendered by a hand-written HTML/CSS/vanilla JS frontend with no framework or build step, including canvas-based charts and a hover-triggered glossary client-side.

[<img src="assets/equity-research-report.gif" width="100%" alt="Equity Research Report live preview">](https://saramarubel.github.io/equity-research-report/)
<p><a href="https://saramarubel.github.io/equity-research-report/">🔗 Live demo</a></p>

### [ETF Basket Analysis](https://github.com/SaraMarubel/ETF-basket-analysis)
A trading-desk-style dashboard covering the 20 largest ETFs by AUM: beta, volatility, Sharpe ratio, max drawdown, tracking error, live bid-ask spreads, and options-market data, plus a 20×20 cross-fund correlation matrix and a holdings-overlap comparison tool. Market and news data refresh every 4 hours via the Yahoo Finance API (`yfinance`) and NewsAPI.org, orchestrated by GitHub Actions. Vanilla HTML/CSS/JS, no framework.

[<img src="assets/ETF-basket-analysis.gif" width="100%" alt="ETF Basket Analysis live preview">](https://saramarubel.github.io/ETF-basket-analysis/)
<p><a href="https://saramarubel.github.io/ETF-basket-analysis/">🔗 Live demo</a></p>

<br>

##  Astrophysics Projects

### [Galaxy Classification](https://github.com/SaraMarubel/galaxy-classification)
Classifies stars, galaxies, and black holes using real astrophysical techniques: the 21 cm hyperfine line for galaxy rotation, effective temperature for stellar spectral typing, and mass / Schwarzschild radius for black hole size classes.

[![Source](https://img.shields.io/badge/Source-Repo-blue?style=for-the-badge)](https://github.com/SaraMarubel/galaxy-classification)

### [Starship Mars Transit: Mission Simulator](https://github.com/SaraMarubel/starship-mars-transit)
A live 3D mission simulator (Three.js): a Starship-style vehicle flies Earth → Mars orbit → Earth on a black-space background, with Earth/Moon/Mars rendered at their true relative size ratio and a mission-control sidebar tracking stage, speed, acceleration, heading, and velocity in real time.

[<img src="assets/starship-mars-transit.gif" width="100%" alt="Starship Mars Transit live preview">](https://saramarubel.github.io/starship-mars-transit/)
<p><a href="https://saramarubel.github.io/starship-mars-transit/">🔗 Live demo</a></p>

<br>

## 🧪 Other builds

### [Customer Interface System: Marubel Pizza's](https://github.com/SaraMarubel/Customer-Interface-system1)
A full pizza-ordering flow demo: branch finder, custom pizza builder, cart, itemised receipt, and a simulated checkout.

[<img src="assets/Customer-Interface-system1.gif" width="100%" alt="Customer Interface System live preview">](https://saramarubel.github.io/Customer-Interface-system1/)
<p><a href="https://saramarubel.github.io/Customer-Interface-system1/">🔗 Live demo</a></p>

<br>

---

<p align="center"><sub>All finance projects above use simulated/paper trading or free public data; none connect to a live brokerage or real funds.</sub></p>
