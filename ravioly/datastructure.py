from math import atan2, cos, radians, sin, sqrt
from typing import Tuple

from pandas import DataFrame, Series, read_csv, to_datetime


class Ravioly(DataFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(read_csv(*args, **kwargs))
        self.pickup_datetime: Series = to_datetime(self.pickup_datetime).dt.tz_localize(
            "US/Eastern"
        )
        self.dropoff_datetime: Series = to_datetime(
            self.dropoff_datetime
        ).dt.tz_localize("US/Eastern")
        self["distance"]: Series = self.apply(self._distance, axis="columns")
        self["avg_speed"]: Series = self.distance / (self.trip_duration / 3600)

    def _haversine_distance(
        self, coords0: Tuple[float, float], coords1: Tuple[float, float]
    ) -> float:
        """
        Implementation of the Haversine formula:
        https://en.wikipedia.org/wiki/Haversine_formula

        :param coords0: first GPS coordinates (latitude, longitude)
        :param coords1: second GPS coordinates (latitude, longitude)
        :return: haversine distance in KM between the two GPS coordinates.

        >>> haversine_distance((0, 0), (0, 0))
        0.0
        >>> haversine_distance((48.87, 2.33), (51.53, -0.24))
        347.72272585658754
        """
        radius: int = 6371  # Earth avg radius

        lat0: float = coords0[0]
        lon0: float = coords0[1]
        lat1: float = coords1[0]
        lon1: float = coords1[1]

        phi0: float = radians(lat0)
        phi1: float = radians(lat1)
        dphi: float = radians(lat1 - lat0)
        dlambda: float = radians(lon1 - lon0)

        a: float = sin(dphi / 2) ** 2 + cos(phi0) * cos(phi1) * sin(dlambda / 2) ** 2
        distance: float = 2 * radius * atan2(sqrt(a), sqrt(1 - a))
        return distance

    def _distance(self, row: Series) -> float:
        """
        Compute distance for a single row (ie. taxi trip)
        return: km
        """
        coords0: Tuple[float, float] = (row.pickup_latitude, row.pickup_longitude)
        coords1: Tuple[float, float] = (row.dropoff_latitude, row.dropoff_longitude)
        return self._haversine_distance(coords0, coords1)
