import os
import unittest
from typing import List
import pandas as pd

from ravioli.datastructure import Ravioli


class TestInitRavioli(unittest.TestCase):
    """Checks that the ravioli class succeeds during init"""

    def setUp(self):
        self.path = os.path.dirname(__file__)
        self.filepath = os.path.join(self.path, "samples.csv")

    def test_init(self):
        df = Ravioli(self.filepath)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIsInstance(df, Ravioli)
        self.assertEqual(df.shape, (40, 11))

    def test_init_args(self):
        columns: List[str] = [
            "pickup_datetime",
            "dropoff_datetime",
            "pickup_longitude",
            "pickup_latitude",
            "dropoff_longitude",
            "dropoff_latitude",
            "trip_duration",
        ]
        df = Ravioli(self.filepath, nrows=26, usecols=columns)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIsInstance(df, Ravioli)
        self.assertEqual(df.shape, (26, 7))
