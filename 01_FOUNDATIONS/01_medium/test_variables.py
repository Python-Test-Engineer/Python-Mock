from unittest.mock import patch  # import patch from unittest.mock file

from variables import Car  # importing Car class from variables file


class TestCar:
    def test_value_with_patch(self):
        # mocking a class variable
        # provide `file_name.class_name.variable_name` as str
        with patch("variables.Car.cost", 5000):
            print("\n", Car.cost)  # this prints 5000
