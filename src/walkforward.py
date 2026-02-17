import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from data_loader import load_data
from signals import momentum_signal
from risk import volatility_scaling


TICKERS = ["SPY", "TLT", "GLD", "DBC"]


def walk_forward_backtest():

    prices, returns = load_data(TICKERS)

    all_returns = pd.Series(index=returns.index)

    years = sorted(list(set(returns.index.year)))

    for i in range(5, len(years)-1):

        train_years = years[:i]
        test_year = years[i]

        train_idx = returns.index.year.isin(train_years)
        test_idx = returns.index.year == test_year

        train_prices = prices[train_idx]
        test_prices = prices[test_idx]

        train_returns = returns[train_idx]
        test_returns = returns[test_idx]

        # Generate signals based only on training information
        signals = momentum_signal(prices)

        positions = volatility_scaling(returns, signals)

        strategy_returns = (positions.shift(1) * returns).mean(axis=1)

        all_returns.loc[test_idx] = strategy_returns.loc[test_idx]

    equity_curve = (1 + all_returns.fillna(0)).cumprod()

    buy_hold = (1 + returns["SPY"]).cumprod()

    return equity_curve, buy_hold


if __name__ == "__main__":

    strategy, buy_hold = walk_forward_backtest()

    plt.figure(figsize=(10,6))
    plt.plot(buy_hold, label="Buy & Hold SPY")
    plt.plot(strategy, label="Walk-Forward Momentum Strategy")

    plt.title("Out-of-Sample Walk Forward Test")
    plt.legend()
    plt.grid(True)
    plt.show()
