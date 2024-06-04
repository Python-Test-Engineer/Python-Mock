from unittest.mock import patch
from pyboxen import boxen
from rich.console import Console

console = Console()

from variables_03 import Car  # importing Car class from variables file

console.print(globals()["Car"].__dict__)


class TestCar:
    def test_value_with_patch(self):
        # mocking a class variable
        # provide `file_name.class_name.attribute_name` as str
        with patch("variables_03.Car.cost", 5000):
            console.print("\nCar.cost", Car.cost)

    def test_get_cost(self):
        # mocking a class method
        # provide `file_name.class_name.attribute_name` as str
        with patch("variables_03.Car.get_cost", return_value=10000):
            console.print("\nCar.get_cost()", Car.get_cost())  # this prints 10000
            # still prints 2000, because we are patching get_cost not cost
            console.print("Car.cost", Car.cost)  # prints 2000 still

    def test_insurance_variable(self):
        # mocking an instance variable
        car1 = Car()
        # "insurance" is present in the car1 instance, so provide the name
        # remember that we have to provide the name of variable in str
        with patch.object(car1, "insurance", new=1000):
            console.print("\ncar1.insurance", car1.insurance)  # prints 1000
