from unittest.mock import patch

# from pyboxen import boxen
from rich.console import Console

from variables_04 import Car  # importing Car class from variables file

console = Console()


class TestCar:
    def test_value_with_patch(self):
        # mocking a class variable
        # provide `file_name.class_name.attribute_name` as str
        with patch("variables_04.Car.cost", 5000):
            console.print("\nCar.cost", Car.cost)

    def test_get_cost(self):
        # mocking a class method
        # provide `file_name.class_name.attribute_name` as str
        with patch("variables_04.Car.get_cost", return_value=5000):
            console.print("\nCar.get_cost()", Car.get_cost())  # this prints 5000
            # still prints 2000, because we are patching get_cost not cost
            console.print("Car.cost", Car.cost)  # prints 2000 still

    def test_insurance_variable(self):
        # mocking an instance variable
        car1 = Car()
        # "insurance" is present in the car1 instance, so provide the name
        # remember that we have to provide the name of variable in str
        with patch.object(car1, "insurance", new=1000):
            console.print("\ncar1.insurance", car1.insurance)  # prints 1000

    def test_insurance_method(self):
        # mocking an instance method
        car = Car()
        # "get_insurance" is present in the car instance, so provide the name
        # remember that we have to provide the name of the method in str
        with patch.object(car, "get_insurance", return_value=3000):
            console.print("\ncar.get_insurance()", car.get_insurance())  # prints 3000
