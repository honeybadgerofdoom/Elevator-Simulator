from elevator import Elevator
from summary import Summary
from trip import Trip
import argparse


def parse_args() -> tuple[int, list[int]]:
    """
    Parse the cli arguments
    :return: parsed start floor and list of floors to visit
    """

    # Define the arg parser
    parser = argparse.ArgumentParser(description="Parse the elevator/trip args")
    parser.add_argument("start", type=str, help="Starting floor like so: start=<int>")
    parser.add_argument("floor", type=str, help="Comma-separated list of floors like this: floor=<int,int,...>")
    args = parser.parse_args()

    # Check args for incorrect format
    if not args.start.startswith("start="):
        raise ValueError("Invalid format for start floor. Use start=<int>")

    # Get the start floor
    start_floor = int(args.start.split("=")[1])

    # Check floors for correct format
    if not args.floor.startswith("floor="):
        raise ValueError("Invalid format for floors to visit. Use floor=<int,int,...>")

    # Get the floors to visit
    floors_to_visit = list(map(int, args.floor.split("=")[1].split(",")))

    # Return
    return start_floor, floors_to_visit


def main():
    try:
        start_floor, floors_to_visit = parse_args()  # Parse cli args
        elevator: Elevator = Elevator()  # Instantiate an Elevator object
        trip: Trip = Trip(start_floor, floors_to_visit)  # Instantiate a Trip object
        result: Summary = elevator.do_trip(trip)  # call do_trip, store the resulting Summary instance
        print(result)  # Call the Summary instance's _repr_ method

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
