# src/data_processing.py

import pandas as pd
import os
from sklearn.model_selection import train_test_split

def load_data(file_path):
    """Loads the dataset from the specified relative or absolute path."""
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
    """Cleans the dataset by handling missing values, duplicates, and invalid entries."""
    # Drop duplicates
    data = data.drop_duplicates()

    # Fill missing numeric columns with 0
    numeric_cols = data.select_dtypes(include=["float64", "int64"]).columns
    data[numeric_cols] = data[numeric_cols].fillna(0)

    # Handle missing datetime values
    if "TransactionStartTime" in data.columns:
        data['TransactionStartTime'] = pd.to_datetime(data['TransactionStartTime'], errors='coerce')

    return data

def split_data(data, target_column, test_size=0.2, random_state=42):
    """
    Splits the dataset into train and test sets.
    Args:
        data (pd.DataFrame): The dataset to split.
        target_column (str): The target variable.
        test_size (float): Proportion of the dataset to include in the test split.
        random_state (int): Random seed for reproducibility.
    Returns:
        tuple: Split datasets (X_train, X_test, y_train, y_test).
    """
    X = data.drop(columns=[target_column])
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def save_split_data(X_train, X_test, y_train, y_test, output_dir):
    """
    Saves the split datasets to the specified directory.
    """
    try:
        os.makedirs(output_dir, exist_ok=True)
        X_train.to_csv(os.path.join(output_dir, "X_train.csv"), index=False)
        X_test.to_csv(os.path.join(output_dir, "X_test.csv"), index=False)
        y_train.to_csv(os.path.join(output_dir, "y_train.csv"), index=False)
        y_test.to_csv(os.path.join(output_dir, "y_test.csv"), index=False)
        print(f"Split data saved to {output_dir}.")
    except Exception as e:
        print(f"Error saving split data: {e}")

# Example Usage
if __name__ == "__main__":
    input_path = r"C:\Users\neba\Documents\credit-scoring-project\data\raw\data.csv"
    output_dir = r"C:\Users\neba\Documents\credit-scoring-project\data\processed"

    # Load and clean data
    df = load_data(input_path)
    if df is not None:
        df_cleaned = clean_data(df)

        # Split data into train and test sets
        X_train, X_test, y_train, y_test = split_data(df_cleaned, target_column="FraudResult")

        # Save the split data
        save_split_data(X_train, X_test, y_train, y_test, output_dir)
