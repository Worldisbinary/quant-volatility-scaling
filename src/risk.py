import numpy as np


def volatility_scaling(returns, signals, target_vol=0.15, lookback=20):

    rolling_vol = returns.rolling(lookback).std() * np.sqrt(252)

    position_size = target_vol / rolling_vol
    position_size = position_size.clip(upper=3)

    positions = signals * position_size

    return positions
