
"""
Container class for storing trip data
"""


class Trip:

    def __init__(self, start_floor: int, floors_to_visit: list[int]):
        self.start_floor = start_floor  # Floor we're starting on
        self.floors_to_visit = floors_to_visit  # All floors we're vising

    def __repr__(self):
        full_trip: list[int] = [self.start_floor] + self.floors_to_visit
        return ",".join(map(str, full_trip))
