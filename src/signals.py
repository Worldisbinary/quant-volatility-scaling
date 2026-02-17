import pandas as pd


def moving_average_signal(data, short_window=50, long_window=200):
    """
    Generates a trend-following signal using moving average crossover.

    Returns:
        DataFrame with signal column (1 = long, 0 = out of market)
    """

    df = data.copy()

    # Moving averages
    df['ma_short'] = df['price'].rolling(window=short_window).mean()
    df['ma_long'] = df['price'].rolling(window=long_window).mean()

    # Signal: 1 if short MA > long MA
    df['signal'] = (df['ma_short'] > df['ma_long']).astype(int)

    return df
