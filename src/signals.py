import pandas as pd


def momentum_signal(prices, lookback=252):
    """
    Time-series momentum:
    If past 12-month return positive → long
    If negative → out
    """

    momentum = prices.pct_change(lookback)

    signal = (momentum > 0).astype(int)

    return signal
