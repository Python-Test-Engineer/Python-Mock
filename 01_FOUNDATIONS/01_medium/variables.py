# https://medium.com/@hema-chandra/mocking-patching-class-instance-variables-in-python-testing-31d1e7447544

from pyboxen import boxen
from rich.console import Console

console = Console()


class Car:
    cost = 2000


console.print("cost of car", Car.cost)  # prints 2000
