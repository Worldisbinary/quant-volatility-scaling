# Quant Project 1 — Volatility Targeted Momentum Portfolio

This project implements a systematic trading strategy based on time-series momentum and volatility targeting.

## Idea
Instead of predicting prices, the strategy dynamically adjusts exposure based on market risk and trend.

Assets traded:
- SPY (Equities)
- TLT (Bonds)
- GLD (Gold)
- DBC (Commodities)

## Methodology
1. 12-month momentum signal
2. Volatility scaling to target constant risk
3. Multi-asset diversification
4. Walk-forward backtesting

## Key Concept
The objective is not to maximize returns but to maximize **risk-adjusted returns** and reduce drawdowns.

## Output
The strategy is compared against a buy-and-hold equity benchmark.

## Skills Demonstrated
- Time-series analysis
- Portfolio construction
- Backtesting framework
- Risk management
- Python (pandas, numpy, matplotlib)

