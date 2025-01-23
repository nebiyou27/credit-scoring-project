# src/utils.py

import pandas as pd

def get_data_overview(data: pd.DataFrame) -> pd.DataFrame:
    """
    Get an overview of the dataset with missing values and their percentages.
    """
    missing_values = data.isnull().sum()
    percentages = (missing_values / len(data)) * 100
    overview = pd.DataFrame({
        "Missing Values": missing_values,
        "Percentage": percentages
    })
    return overview

def has_missing_values(data: pd.DataFrame) -> bool:
    """
    Check if the dataset contains any missing values.
    """
    return data.isnull().values.any()
