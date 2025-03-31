from trip import Trip

"""
Container class containing summary data to be printed as final output
"""


class Summary:

    def __init__(self, trip: Trip, total_time: int):
        self.trip = trip
        self.total_time = total_time

    def __repr__(self):
        return f"{self.total_time} {self.trip}"
