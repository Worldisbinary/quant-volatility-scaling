import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from data_loader import load_data
from signals import moving_average_signal
from risk import apply_volatility_targeting


def run_backtest(ticker="SPY"):

    # 1. Load data
    data = load_data(ticker)

    # 2. Generate signals
    data = moving_average_signal(data)

    # 3. Apply volatility targeting
    data = apply_volatility_targeting(data)

    # 4. Strategy returns
    data['strategy_returns'] = data['position'].shift(1) * data['returns']

    # 5. Equity curve
    data['equity_curve'] = (1 + data['strategy_returns']).cumprod()

    # Buy & Hold comparison
    data['buy_hold'] = (1 + data['returns']).cumprod()

    return data


def performance_metrics(data):

    returns = data['strategy_returns'].dropna()

    sharpe = np.sqrt(252) * returns.mean() / returns.std()

    # Max Drawdown
    equity = data['equity_curve']
    peak = equity.cummax()
    drawdown = (equity - peak) / peak
    max_dd = drawdown.min()

    return sharpe, max_dd


if __name__ == "__main__":

    data = run_backtest()

    sharpe, max_dd = performance_metrics(data)

    print("Sharpe Ratio:", round(sharpe, 2))
    print("Max Drawdown:", round(max_dd, 2))

    # Plot equity curve
    plt.figure(figsize=(10,6))
    plt.plot(data['equity_curve'], label="Volatility Scaled Strategy")
    plt.plot(data['buy_hold'], label="Buy & Hold")
    plt.title("Strategy vs Buy & Hold")
    plt.legend()
    plt.grid(True)

    # Save plot
    plt.savefig("../results/equity_curve.png")

    plt.show()
