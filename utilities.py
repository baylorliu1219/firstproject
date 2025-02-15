import yfinance as yf
import pandas as pd
from typing import Optional


# 让 Pandas 显示所有列
pd.set_option("display.max_columns", None)  
pd.set_option("display.width", 200)  

def fetch_stock_data(
    ticker: str,
    period: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> pd.DataFrame:
    """
    Fetch historical stock data for a specific ticker from Yahoo Finance.

    Parameters:
        ticker (str): Stock ticker symbol.
        period (Optional[str]): Period string for Yahoo Finance API (e.g., '1d', '1mo', '3mo', '1y').
        start_date (Optional[str]): Start date as 'YYYY-MM-DD'.
        end_date (Optional[str]): End date as 'YYYY-MM-DD'.

    Returns:
        pd.DataFrame: DataFrame with historical stock data.
    """
    stock = yf.Ticker(ticker)

    if period:
        df = stock.history(period=period)
    elif start_date and end_date:
        df = stock.history(start=start_date, end=end_date)
    else:
        raise ValueError("Either 'period' or both 'start_date' and 'end_date' must be provided.")

    # Reset index to have 'Date' as a column
    df.reset_index(inplace=True)

    return df

if __name__ == "__main__":
    # Fetch 1-day stock data for AAPL
    res1 = fetch_stock_data("AAPL", period="1d")
    print("\nAAPL Stock Data (Last 1 Day):")
    print(res1.head())

    # Fetch stock data for AAPL from January 1, 2021 to January 31, 2021
    res2 = fetch_stock_data("AAPL", start_date="2021-01-01", end_date="2021-01-31")
    print("\nAAPL Stock Data (January 2021):")
    print(res2.head())
