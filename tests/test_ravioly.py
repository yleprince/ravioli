import os
import unittest
from typing import List

import pandas as pd
from ravioly.datastructure import Ravioly


class TestInitravioly(unittest.TestCase):
    """Tests that the ravioly class succeeds during init"""

    def setUp(self):
        self.path = os.path.dirname(__file__)
        self.filepath = os.path.join(self.path, "samples.csv")

    def test_init(self):
        df: Ravioly = Ravioly(self.filepath)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIsInstance(df, Ravioly)
        self.assertEqual(df.shape, (40, 13))

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
        self.assertEqual(df.shape, (26, 9))
        self.assertTrue("distance" in df.columns)
        self.assertTrue("avg_speed" in df.columns)


class TestDistanceComputations(unittest.TestCase):
    """Tests that the Ravioly class succeeds during init to compute the distance
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

        # d(Paris - London) is 347 km
        self.assertEqual(
            Ravioly._haversine_distance(self, (48.87, 2.33), (51.53, -0.24)),
            347.72272585658754,
        )


class TestAverageSpeedComputations(unittest.TestCase):
    """Tests that the Ravioly class succeeds during init to compute average
     speeds between the pickup and the drop off coordinates."""

    def setUp(self):
        self.path = os.path.dirname(__file__)
        self.filepath = os.path.join(self.path, "samples.csv")

    def test_avg_speed_values(self):
        df: Ravioly = Ravioly(self.filepath)
        expected: List[float] = [
            11.856428,
            9.803659,
            10.822201,
            12.465721,
            9.836594,
            8.930458,
            14.001768,
            13.264945,
            18.499105,
            15.049944,
            10.755182,
            12.041796,
            6.009101,
            13.731021,
            16.250501,
            11.202279,
            5.328631,
            12.502351,
            12.588249,
            18.692336,
            18.562416,
            9.522056,
            17.592212,
            15.089641,
            29.846789,
            12.793679,
            19.293800,
            19.394051,
            10.189974,
            15.350491,
            11.110572,
            18.628805,
            15.848751,
            16.244242,
            7.297254,
            10.213026,
            7.397850,
            12.469197,
            10.029165,
            6.116273,
        ]
        for value, target in zip(df.avg_speed.values, expected):
            self.assertAlmostEqual(value, target, delta=0.0001)


class TestTripByDayOfWeek(unittest.TestCase):
    """Tests the method trip_by_dow that counts the number of trip by weekday."""

    def setUp(self):
        self.path = os.path.dirname(__file__)
        self.filepath = os.path.join(self.path, "samples.csv")

    def test_trip_by_dow(self):
        df: Ravioly = Ravioly(self.filepath)
        expected: List[int] = [6, 6, 3, 3, 8, 8, 6]
        for value, target in zip(df.trip_by_dow().values, expected):
            self.assertEqual(value, target)
        self.assertEqual(df.trip_by_dow().name, "trip_by_dow")
