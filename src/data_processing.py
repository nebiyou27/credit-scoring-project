# src/data_processing.py

import pandas as pd
import os

def load_data(file_path):
    """
    Loads the dataset from the specified relative or absolute path.
    Args:
        file_path (str): Path to the dataset.
    Returns:
        pd.DataFrame: Loaded dataset as a DataFrame.
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(data):
    """
    Cleans the dataset by handling missing values, duplicates, and invalid entries.
    Args:
        data (pd.DataFrame): Raw data to be cleaned.
    Returns:
        pd.DataFrame: Cleaned data.
    """
    # Drop duplicates
    data = data.drop_duplicates()

    # Fill missing numeric columns with 0
    numeric_cols = data.select_dtypes(include=["float64", "int64"]).columns
    data[numeric_cols] = data[numeric_cols].fillna(0)

    # Handle missing datetime values
    if "TransactionStartTime" in data.columns:
        data['TransactionStartTime'] = pd.to_datetime(data['TransactionStartTime'], errors='coerce')

    return data

def save_processed_data(data, output_path):
    """
    Saves the cleaned and processed data to the specified path.
    Args:
        data (pd.DataFrame): The data to save.
        output_path (str): Path to save the processed data.
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        data.to_csv(output_path, index=False)
        print(f"Processed data saved to {output_path}.")
    except Exception as e:
        print(f"Error saving data: {e}")

# Example Usage
if __name__ == "__main__":
    # Relative paths based on the folder structure
    input_path = "../data/raw/data.csv"
    output_path = "../data/processed/cleaned_data.csv"

    df = load_data(input_path)
    if df is not None:
        cleaned_df = clean_data(df)
        save_processed_data(cleaned_df, output_path)
