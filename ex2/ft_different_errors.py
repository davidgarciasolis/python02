#!/usr/bin/python3
def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            (int)("abc")
        case 1:
            10/0
        case 2:
            open("abc")
        case 3:
            "Tengo " + 25 + " años" # type: ignore
        case _:
            return


def test_error_rypes() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(0, 4):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueErro: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeErro: {e}")
    print()
    print("All error types tested successfully!")


def main() -> None:
    test_error_rypes()


if __name__ == "__main__":
    test_error_rypes()
