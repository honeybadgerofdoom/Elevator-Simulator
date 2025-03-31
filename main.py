from elevator import Elevator
from trip import Trip

if __name__ == '__main__':
    elevator = Elevator()
    trip1 = Trip(12, [2, 9, 1, 32])
    result = elevator.do_trip(trip1)
    print(f"Trip1 result: {result}")