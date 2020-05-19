import os
import unittest
from typing import List

import pandas as pd

from ravioly.datastructure import Ravioly


class TestInitravioly(unittest.TestCase):
    """Checks that the ravioly class succeeds during init"""

    def setUp(self):
        self.path = os.path.dirname(__file__)
        self.filepath = os.path.join(self.path, "samples.csv")

    def test_init(self):
        df: Ravioly = Ravioly(self.filepath)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIsInstance(df, Ravioly)
        self.assertEqual(df.shape, (40, 12))

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
        df: Ravioly = Ravioly(self.filepath, nrows=26, usecols=columns)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIsInstance(df, Ravioly)
        self.assertEqual(df.shape, (26, 8))
        self.assertTrue("distance" in df.columns)


class TestDistanceComputations(unittest.TestCase):
    """Checks that the Ravioly class succeeds during init to compute the distance
     between the pickup and the drop off coordinates."""

    def setUp(self):
        self.path = os.path.dirname(__file__)
        self.filepath = os.path.join(self.path, "samples.csv")

    def test_distance_values(self):
        df: Ravioly = Ravioly(self.filepath)
        expected: List[float] = [
            1.498521,
            1.805507,
            6.385098,
            1.485498,
            1.188588,
            1.098942,
            1.326279,
            5.714981,
            1.310353,
            5.121162,
            3.806139,
            3.773096,
            1.859483,
            0.991685,
            6.382836,
            0.656578,
            3.428086,
            2.538672,
            4.605201,
            1.303271,
            2.505926,
            1.724550,
            2.067085,
            4.874792,
            20.602575,
            4.559525,
            6.056109,
            3.738742,
            2.524849,
            9.939443,
            4.564593,
            5.423052,
            4.499284,
            10.238385,
            1.433100,
            1.492237,
            1.136392,
            0.959435,
            3.312410,
            2.587523,
        ]
        for value, target in zip(df.distance.values, expected):
            self.assertAlmostEqual(value, target, delta=0.0001)

    def test_haversine_distance(self):
        self.assertEqual(Ravioly._haversine_distance(self, (0, 0), (0, 0)), 0.0)
        self.assertEqual(
            Ravioly._haversine_distance(self, (48.87, 2.33), (51.53, -0.24)),
            347.72272585658754,
        )
