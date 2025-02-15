from typing import Optional
import pandas as pd 

def ticker_data_processing(
    mode: str,
    ticker: str,
    model,
    start_date: Optional[pd.Timestamp] = None,
    end_date: Optional[pd.Timestamp] = None,
    longest_period: Optional[str] = None,
) -> pd.DataFrame:
    """
    Fetch ticker data based on the mode and date range.

    Parameters:
        mode (str): 'initial', 'daily', or 'rerun'
        start_date (Optional[pd.Timestamp]): Start date for rerun mode.
        end_date (Optional[pd.Timestamp]): End date for rerun mode.

    Returns:
        pd.DataFrame: DataFrame with ticker data.
    """
    # if mode is "initial":
        # fetch data using longest_period( 1y, 3y, etc)
        # write to sqlite db(calling the function you just created in step 1)
    
    # if mode is daily:
       # fetch data for just 1 day
       # write to db