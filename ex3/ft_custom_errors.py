#!/usr/bin/python3
class GardenError(Exception):
    def __init__(self, menssage="Unknown garden error"):
        super().__init__(menssage)


class WaterError(GardenError):
    def __init__(self, menssage="Unknown water error"):
        super().__init__(menssage)


class PlantError(GardenError):
    def __init__(self, menssage="Unknown plant error"):
        super().__init__(menssage)


def check_water() -> None:
    raise WaterError("Not enough water in the tank!")


def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")
    try:
        check_plant()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
