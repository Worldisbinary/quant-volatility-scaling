import yfinance as yf
import pandas as pd


def load_data(ticker="SPY", start="2010-01-01"):
    """
    Downloads historical price data and computes returns.
    """
    data = yf.download(ticker, start=start)
    data = data[['Adj Close']].copy()
    data.rename(columns={'Adj Close': 'price'}, inplace=True)

    data['returns'] = data['price'].pct_change()

    return data
