# Elevator Simulator

This project simulates an elevator. The time taken to travel between each floor is exactly 10 (seconds). Use this to
calculate the time taken to travel between arbitrary floors using this elevator

## Assumptions

- The elevator always travels at the same speed
- The elevator doesn't actually pause when it reaches a floor
- The elevator turns around instantly, i.e. there is no time lost to transitioning from upwards to downwards movement
- Floors are whole numbers. There are no fractional floors.

## Usage

This project is built with `Python`, you'll need python installed locally to run it! It was built on `Python 3.11.0`

### Args
- `start <int>` the start floor for the trip
- `floor <list<int>>` the list of floors to visit, comma-separated

### Example
- `python3 main.py start=12 floor=2,9,1,32`

## Testing

- Run `python3 test.py` for some simple tests
