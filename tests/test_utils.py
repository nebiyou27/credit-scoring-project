# tests/test_utils.py

import unittest
import pandas as pd
from src.utils import get_data_overview, has_missing_values

class TestUtils(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        self.data_with_missing = pd.DataFrame({
            "A": [1, 2, None, 4],
            "B": [None, 2, 3, 4],
            "C": [1, 2, 3, 4]
        })
        self.data_no_missing = pd.DataFrame({
            "A": [1, 2, 3, 4],
            "B": [5, 6, 7, 8],
            "C": [9, 10, 11, 12]
        })

    def test_get_data_overview(self):
        # Test missing values overview
        overview = get_data_overview(self.data_with_missing)
        self.assertEqual(overview.loc["A", "Missing Values"], 1)
        self.assertEqual(overview.loc["B", "Missing Values"], 1)
        self.assertEqual(overview.loc["C", "Missing Values"], 0)

    def test_has_missing_values(self):
        # Test presence of missing values
        self.assertTrue(has_missing_values(self.data_with_missing))
        self.assertFalse(has_missing_values(self.data_no_missing))
