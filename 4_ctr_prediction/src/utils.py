import pandas as pd
from pathlib import Path
from typing import Tuple
from src.config import *

def data_loader(file_path) -> pd.DataFrame:
    '''
    loads the file as a dataframe from given file_path

    Args:
        file_path: path to the csv file

    Returns:
        pd.DataFrame: data loaded onto dataframe
    '''
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError('File not found, retry with a different file')
    
    if file_path.suffix.lower() != '.csv':
        raise ValueError('File is not of CSV format, upload a csv file')
    
    df = pd.read_csv(file_path) # load the data onto a dataframe

    return df 


def feature_engineering(cleansed_df: pd.DataFrame) -> pd.DataFrame:
    '''
    performs feature engineering to generate necessary features based on existing columns

    Args:
        cleansed_df: cleansed dataframe

    Returns:
        pd.DataFrame: updated dataframe with necessary engineered features
    '''
    # feature engineering on train-data
    processed_df = cleansed_df.copy()

    # Ensure hour column exists
    if "hour" not in processed_df.columns:
        raise KeyError("'hour' column is missing from dataframe")

    processed_df["hour"] = processed_df["hour"].astype(str).str.strip() # Convert to string safely

    invalid_hour_mask = ~processed_df["hour"].str.match(r"^\d{8}$")   # Handle invalid hour formats Expected format: YYMMDDHH (8 digits)

    if invalid_hour_mask.any():
        print(
            f"Warning: {invalid_hour_mask.sum()} invalid hour values detected."
        )
    
    processed_df.loc[invalid_hour_mask, "hour"] = None # Convert invalid rows to NaN before datetime conversion

    # Safe datetime conversion
    processed_df["datetime"] = pd.to_datetime(
        processed_df["hour"],
        format="%y%m%d%H",
        errors="coerce"  # invalid parsing -> NaT
    )

    invalid_datetime_count = processed_df["datetime"].isna().sum() # Warn if parsing failed

    if invalid_datetime_count > 0:
        print(
            f"Warning: {invalid_datetime_count} rows contain invalid datetime values."
        )
    
    processed_df["hour_of_day"] = processed_df["datetime"].dt.hour # Feature engineering
    processed_df["day_of_week"] = processed_df["datetime"].dt.dayofweek # Monday = 0, Sunday = 6
    processed_df["weekend_flag"] = (
        processed_df["day_of_week"]
        .apply(lambda x: 1 if pd.notna(x) and x >= 5 else 0)
    ) # Weekend flag

    return processed_df

def data_splitter(processed_df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    '''
    Splits the processed dataframe into X_train, X_test, y_train, y_test

    Args:
        processed_df: Processed dataframe with necessary engineered features

    Returns:
        X_train
        X_test
        y_train
        y_test
    '''
    X = processed_df[features].copy() # input columns aka feature set
    y = processed_df[target] # output column aka target

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X,y,
                                                    test_size=test_size,
                                                    random_state=random_state,
                                                    stratify=y)
    return X_train, X_test, y_train, y_test
