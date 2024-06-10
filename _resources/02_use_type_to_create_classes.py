from pyboxen import boxen

from rich.console import Console

console = Console()


class_name = "Square"

class_body = """
def __init__(self, x, y):
    self.x = x
    self.y = y


def area(self):
    return self.x * self.y
"""

class_bases = ()  # defaults to object

class_dict = {}

exec(class_body, globals(), class_dict)

console.print(class_dict)

Square = type(class_name, class_bases, class_dict)

square = Square(2, 4)

console.print(square.x, square.y)

console.print(square.area())
