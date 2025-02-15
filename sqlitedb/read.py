import pandas as pd 
def read_data_from_sqlite(model) -> pd.DataFrame:

    """
    Read data from a SQLite table using ORM model with optional filters and date range.
    
    Returns:
        pd.DataFrame: DataFrame containing the query results.
    """
