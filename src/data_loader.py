import yfinance as yf
import pandas as pd


def load_data(ticker="SPY", start="2010-01-01"):
    """
    Downloads historical price data and computes returns.
    """

    data = yf.download(ticker, start=start, auto_adjust=True)

    # Use Close price (already adjusted when auto_adjust=True)
    data = data[['Close']].copy()
    data.rename(columns={'Close': 'price'}, inplace=True)

    # daily returns
    data['returns'] = data['price'].pct_change()

    # remove missing values
    data.dropna(inplace=True)

    return data
