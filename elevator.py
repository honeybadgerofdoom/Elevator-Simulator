from summary import Summary
from trip import Trip

DEBUG = False


class Elevator:

    def __init__(self):
        self.speed = 10  # Seconds per floor

    def _travel(self, start: int, end: int):
        """
        Calculate the time taken between two floors
        :param start: starting floor
        :param end: end floor
        :return: the time to travel between stat and end, based on self.speed
        """
        if DEBUG:
            print(f"\tTravelling from {start} to {end}, {self.speed} per seconds floor")
            print(f"\tTotal floors: {abs(start - end)}")
            print(f"\tTotal time: {abs(start - end) * self.speed}")
        return abs(start - end) * self.speed

    def do_trip(self, trip: Trip) -> Summary:
        """
        Travel to all floors in the specified order
        :param trip: The trip objects
        :return: Time taken to travel to all floors and complete the trip
        """

        # Add the initial floor to the array
        visit_array: list[int] = [trip.start_floor] + trip.floors_to_visit

        if DEBUG:
            print(f"\tEntire trip including start: {visit_array}")

        # Calculate total time using reducer from functools
        total_time: int = 0
        for index, current_floor in enumerate(visit_array[0: len(visit_array) - 1]):
            end_floor = visit_array[index + 1]
            total_time += self._travel(current_floor, end_floor)

        # Create & return a summary object instance
        return Summary(trip, total_time)
