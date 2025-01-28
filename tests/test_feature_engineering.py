import pytest
import pandas as pd
from src.feature_engineering import bin_numerical_features, scale_features, one_hot_encode

def test_bin_numerical_features():
    df = pd.DataFrame({'Amount': [100, 200, 500, 1000, 5000]})
    df_binned = bin_numerical_features(df, 'Amount', bins=[0, 100, 1000, 10000], labels=['Low', 'Medium', 'High'])
    assert df_binned['Amount_binned'].iloc[0] == 'Low'
    assert df_binned['Amount_binned'].iloc[1] == 'Medium'
    assert df_binned['Amount_binned'].iloc[3] == 'Medium'
    assert df_binned['Amount_binned'].iloc[4] == 'High'

def test_scale_features():
    df = pd.DataFrame({'Amount': [100, 200, 500, 1000, 5000]})
    df_scaled = scale_features(df, 'Amount')
    assert df_scaled['Amount'].iloc[0] != 100  # Check if the scaling changed the values
    assert df_scaled['Amount'].iloc[1] != 200  # Ensure scaling is applied

def test_one_hot_encode():
    df = pd.DataFrame({'Category': ['A', 'B', 'A', 'C', 'B']})
    df_encoded, encoder = one_hot_encode(df, ['Category'])
    assert 'Category_A' in df_encoded.columns 
    assert 'Category_B' in df_encoded.columns
    assert 'Category_C' in df_encoded.columns 