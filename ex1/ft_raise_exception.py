#!/usr/bin/python3
def input_temperature(temp_str: str) -> int:
    temp_min: int
    temp_max: int
    temp_int: int

    temp_int = int(temp_str)
    temp_min = 0
    temp_max = 40
    if (temp_int <= temp_min):
        raise Exception(
            f"{temp_int}°C is too cold for plants (min {temp_min}°C)"
        )
    elif (temp_int >= temp_max):
        raise Exception(
            f"{temp_int}°C is too hot for plants (max {temp_max}°C)"
        )
    return (temp_int)


def test_temperature(temp_str: str) -> None:
    temp_int: int

    try:
        temp_int = input_temperature(temp_str)
        print(f"Temperature is now {temp_int}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")


def main() -> None:
    tests = ["25", "abc", "100", "-50"]

    print("=== Garden Temperature ===")
    print()
    for t in tests:
        print(f"Input data is '{t}'")
        test_temperature(t)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
