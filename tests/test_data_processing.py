# tests/test_data_processing.py

import unittest
import os
import pandas as pd
from src.data_processing import load_data, clean_data

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        # Set up paths and test data
        self.test_raw_path = "data/raw/data.csv"
        self.test_processed_path = "data/processed/cleaned_data.csv"

        # Create a test CSV file
        self.test_data = pd.DataFrame({
            "A": [1, 2, None, 4],
            "B": [None, 2, 3, 4],
            "C": [1, 2, 3, 4]
        })
        os.makedirs("data/raw", exist_ok=True)
        self.test_data.to_csv(self.test_raw_path, index=False)

    def test_load_data(self):
        """
        Test the load_data function.
        """
        data = load_data(self.test_raw_path)
        self.assertEqual(len(data), 4)  # Check if 4 rows are loaded
        self.assertIn("A", data.columns)  # Ensure column 'A' exists

    def test_clean_data(self):
        """
        Test the clean_data function.
        """
        data = load_data(self.test_raw_path)
        cleaned_data = clean_data(data)
        self.assertFalse(cleaned_data.isnull().values.any())  # No missing values

    def tearDown(self):
        # Clean up after tests
        if os.path.exists(self.test_raw_path):
            os.remove(self.test_raw_path)
