#!/usr/bin/python3
def input_temperature(temp_str: str) -> int:
    return (int)(temp_str)


def test_temperature(temp_str: str) -> None:
    try:
        temp_int = input_temperature(temp_str)
        print(f"Temperature is now {temp_int}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")


def main() -> None:
    tests = ["25", "abc"]

    print("=== Garden Temperature ===")
    print()
    for t in tests:
        print(f"Input data is '{t}'")
        test_temperature(t)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
