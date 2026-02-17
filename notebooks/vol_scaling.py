import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Download data
data = yf.download("SPY", start="2010-01-01")
data = data[['Adj Close']]
data['returns'] = data['Adj Close'].pct_change()

# Moving averages
data['ma50'] = data['Adj Close'].rolling(50).mean()
data['ma200'] = data['Adj Close'].rolling(200).mean()

# Signal
data['signal'] = np.where(data['ma50'] > data['ma200'], 1, 0)

# Rolling volatility (20-day)
data['vol'] = data['returns'].rolling(20).std() * np.sqrt(252)

# Target annual volatility
target_vol = 0.15

# Volatility scaling
data['position'] = data['signal'] * (target_vol / data['vol'])
data['position'] = data['position'].clip(upper=3)  # prevent leverage explosion

# Strategy returns
data['strategy_return'] = data['position'].shift(1) * data['returns']

# Cumulative returns
data['cum_strategy'] = (1 + data['strategy_return']).cumprod()
data['cum_buyhold'] = (1 + data['returns']).cumprod()

# Plot
plt.figure(figsize=(12,6))
plt.plot(data['cum_strategy'], label="Vol Scaled Strategy")
plt.plot(data['cum_buyhold'], label="Buy & Hold")
plt.legend()
plt.show()
