from pandas import DataFrame, Series, read_csv, to_datetime


class Ravioli(DataFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(read_csv(*args, **kwargs))
        self.pickup_datetime: Series = to_datetime(self.pickup_datetime).dt.tz_localize(
            "US/Eastern"
        )
        self.dropoff_datetime: Series = to_datetime(
            self.dropoff_datetime
        ).dt.tz_localize("US/Eastern")
