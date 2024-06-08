from unittest.mock import patch
from pyboxen import boxen
from rich.console import Console
from variables_02 import Car  # importing Car class from variables file

console = Console()

console.print(globals()["Car"].__dict__)


class TestCar:
    def test_value_with_patch(self):
        # mocking a class variable
        # provide `file_name.class_name.attribute_name` as str
        with patch("variables_02.Car.cost", 5000):
            console.print("\nCar.cost", Car.cost)

    def test_get_cost(self):
        # mocking a class method
        # provide `file_name.class_name.attribute_name` as str
        # return_value tells the what to return for the get_cost()
        with patch("variables_02.Car.get_cost", return_value=10000):
            console.print("\nCar.get_cost()", Car.get_cost())  # this prints 10000
            # still prints 2000, because we are patching get_cost not cost
            console.print("Car.cost", Car.cost)  # prints 2000 still
