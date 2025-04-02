import subprocess


def main():
    print("Beginning tests...")
    test1 = run_test(1, [2], 10)  # Go up 1 floor
    test2 = run_test(2, [1], 10)  # Go down 1 floor
    test3 = run_test(1, [-1], 20)  # Go down 2 floors visit a negative (basement) floor
    test4 = run_test(12, [2,9,1,32], 560)  # Example from email

    print(f"Test 1: {test1[1]}")
    print(f"Test 2: {test2[1]}")
    print(f"Test 3: {test3[1]}")
    print(f"Test 4: {test4[1]}")

def run_test(start: int, floors: list[int], expected: int) -> tuple[bool, str]:
    floor = ",".join(map(str, floors))
    test = ["python3", "main.py", f"start={start}", f"floor={floor}"]
    result = subprocess.run(test, capture_output=True, text=True)
    if len(result.stderr) > 0:
        return False, "❌ Test Failed. Error thrown"
    output = result.stdout
    time_taken = int(output.split(" ")[0])
    if time_taken != expected:
        return False, "❌ Test Failed. Incorrect time taken"
    floors_visited = (output.split(" ")[1]).strip()
    full_trip: str = ",".join(map(str, [start] + floors)).strip()
    if floors_visited != full_trip:
        return False, "❌ Test Failed. Incorrect floors visited"
    return True, "✅ Test Passed"


if __name__ == '__main__':
    main()
