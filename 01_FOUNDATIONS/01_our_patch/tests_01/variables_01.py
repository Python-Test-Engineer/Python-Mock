# https://medium.com/@hema-chandra/mocking-patching-class-instance-variables-in-python-testing-31d1e7447544

from pyboxen import boxen
from rich.console import Console

console = Console()


class Car:
    """Setting class variable"""

    cost = 2000


output = f"[blue]In variables.py {Car.cost}[/]"
print("\n")
print(
    boxen(
        output,
        title="[blue]ORIGINAL VALUES[/]",  # closing tag can just be a '/'
        title_alignment="left",  # left center right
        subtitle="[blue]ORIGINAL VALUES[/blue]",
        subtitle_alignment="right",  # left center right
        color="red",
        padding=1,
        fullwidth=True,  # sometimes does not seem to give full console width
    )
)
# if __name__ == "__main__":
#     console.print("cost of car", Car.cost)  # prints 2000
