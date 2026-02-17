import yfinance as yf
import pandas as pd


def load_data(tickers, start="2010-01-01"):
    """
    Downloads multiple asset price data and computes returns.
    """

    data = yf.download(tickers, start=start, auto_adjust=True)['Close']

    # If single column, convert to DataFrame
    if isinstance(data, pd.Series):
        data = data.to_frame()

    # Daily returns
    returns = data.pct_change()

    return data, returns
