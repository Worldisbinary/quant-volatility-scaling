import numpy as np
import matplotlib.pyplot as plt

from data_loader import load_data
from signals import momentum_signal
from risk import volatility_scaling


TICKERS = ["SPY", "TLT", "GLD", "DBC"]


def run_backtest():

    # Load data
    prices, returns = load_data(TICKERS)

    # Signals
    signals = momentum_signal(prices)

    # Risk scaling
    positions = volatility_scaling(returns, signals)

    # Portfolio returns (equal-weighted across assets)
    strategy_returns = (positions.shift(1) * returns).mean(axis=1)

    equity_curve = (1 + strategy_returns).cumprod()

    # Buy & Hold SPY comparison
    buy_hold = (1 + returns["SPY"]).cumprod()

    return equity_curve, buy_hold


if __name__ == "__main__":

    equity_curve, buy_hold = run_backtest()

    plt.figure(figsize=(10,6))
    plt.plot(buy_hold, label="Buy & Hold SPY")
    plt.plot(equity_curve, label="Multi-Asset Momentum Portfolio")

    plt.title("Multi-Asset Momentum vs Equity Market")
    plt.legend()
    plt.grid(True)

    plt.savefig("../results/multi_asset.png")
    plt.show()
