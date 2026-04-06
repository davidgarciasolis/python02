#!/usr/bin/python3
class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water:'{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
	print("=== Garden Watering System ===")
	print()
	print("Testing valid plants...")
	print("Opening watering system")
	try:
		valid_plants = ["Tomato", "Lettuce", "Carrots"]
		for plant in valid_plants:
			water_plant(plant)
	finally:
		print("Closing watering system")
		print()
	print("Testing invalid plants...")
	print("Opening watering system")
	try:
		invalid_plants = ["Tomato", "lettuce", "Carrots"]
		for plant in invalid_plants:
			try:
				water_plant(plant)
			except PlantError as e:
				print(f"Caught PlantError: {e}")
				print(".. ending tests and returning to main")
				return  # stop test on first error
	finally:
		print("Closing watering system")
		print()
		print("Cleanup always happens, even with errors!")


def main() -> None:
    test_watering_system()


if __name__ == "__main__":
    main()