from unittest.mock import patch  # import patch from unittest.mock file
from pyboxen import boxen
from rich.console import Console
from variables_01 import Car

console = Console()

# importing Car class from variables file
#

console.print(globals()["Car"].__dict__)


class TestCar:

    def test_value_with_patch(self):
        # console.print("locals", locals())
        # mocking a class variable
        # provide `file_name.class_name.variable_name` as str

        with patch("variables_01.Car.cost", 5000):
            console.print("\n\tcost of car", Car.cost)  # this prints 5000
