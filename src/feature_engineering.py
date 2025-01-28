import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def bin_numerical_features(data, column, bins, labels):
    """
    Bins numerical data into categories.

    Args:
        data (pd.DataFrame): The input dataset.
        column (str): The column to bin.
        bins (list): List of bin edges.
        labels (list): List of labels for the bins.

    Returns:
        pd.DataFrame: Dataset with binned values.
    """
    data[column + '_binned'] = pd.cut(data[column], bins=bins, labels=labels)
    return data

def scale_features(data, column):
    """
    Scales numerical features using standard scaling.

    Args:
        data (pd.DataFrame): The input dataset.
        column (str): The column to scale.

    Returns:
        pd.DataFrame: Dataset with scaled values.
    """
    scaler = StandardScaler()
    data[column] = scaler.fit_transform(data[[column]]) 
    return data

def one_hot_encode(data, categorical_columns):
    """
    Performs one-hot encoding on categorical features.

    Args:
        data (pd.DataFrame): The input dataset.
        categorical_columns (list): List of categorical feature columns.

    Returns:
        pd.DataFrame: Dataset with one-hot encoded features.
        OneHotEncoder: Fitted encoder for reuse.
    """
    encoder = OneHotEncoder(sparse_output=False) 
    encoded = encoder.fit_transform(data[categorical_columns])
    encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(categorical_columns))
    data = data.join(encoded_df)
    return data, encoder