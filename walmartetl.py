# etl_pipeline.py
import pandas as pd
import os

# 1. Extract

def extract(store_data: pd.DataFrame, extra_data_path: str) -> pd.DataFrame:
    """
    Merges store transaction data with external metadata using the 'index' column.
    """
    extra_df = pd.read_parquet(extra_data_path)
    merged_df = store_data.merge(extra_df, on="index")
    return merged_df

# 2. Transform

def transform(raw_data: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and filters the merged data:
    - Fills missing values using forward fill
    - Extracts 'Month' from 'Date'
    - Filters rows with Weekly_Sales > 10,000
    - Keeps only necessary columns
    """
    raw_data = raw_data.fillna(method='ffill')
    raw_data['Month'] = pd.to_datetime(raw_data['Date']).dt.month
    raw_data = raw_data[raw_data['Weekly_Sales'] > 10000]

    clean_data = raw_data[[
        "Store_ID", "Month", "Dept", "IsHoliday", "Weekly_Sales", "CPI", "Unemployment"
    ]]
    return clean_data

# 3. Aggregate

def avg_weekly_sales_per_month(clean_data: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates average weekly sales per month and renames the column to 'Avg_Sales'.
    """
    agg_data = (
        clean_data[["Month", "Weekly_Sales"]]
        .groupby("Month")
        .agg(Avg_Sales=("Weekly_Sales", "mean"))
        .reset_index()
        .round(2)
    )
    return agg_data

# 4. Load

def load(full_data: pd.DataFrame, full_data_file_path: str, 
         agg_data: pd.DataFrame, agg_data_file_path: str) -> None:
    """
    Saves the cleaned and aggregated data to CSV files without index.
    """
    full_data.to_csv(full_data_file_path, index=False)
    agg_data.to_csv(agg_data_file_path, index=False)

# 5. Validate

def validation(file_path: str) -> bool:
    """
    Checks whether a file exists at the given path.
    """
    return os.path.exists(file_path)
