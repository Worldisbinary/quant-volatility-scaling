import numpy as np


def apply_volatility_targeting(data, target_vol=0.15, lookback=20, max_leverage=3):
    """
    Scales position size based on rolling realized volatility.

    target_vol: desired annualized volatility (e.g. 15%)
    lookback: rolling window for volatility estimate
    """

    df = data.copy()

    # Rolling annualized volatility
    df['rolling_vol'] = df['returns'].rolling(lookback).std() * np.sqrt(252)

    # Position sizing
    df['position_size'] = target_vol / df['rolling_vol']

    # Avoid infinite leverage when vol is tiny
    df['position_size'] = df['position_size'].clip(upper=max_leverage)

    # Apply trading signal
    df['position'] = df['signal'] * df['position_size']

    return df
