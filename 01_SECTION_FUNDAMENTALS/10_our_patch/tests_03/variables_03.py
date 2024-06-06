from pyboxen import boxen
from rich.console import Console

console = Console()


class Car:
    cost = 2000

    def __init__(self):
        # creating an instance variable
        self.insurance = 5000

    @classmethod
    def get_cost(cls):
        return cls.cost

    def get_insurance(self):
        return self.insurance


car = Car()

output = f"[blue]Car.cost {Car.cost}[/]"
output += f"\n[green]Car.get_cost() {Car.get_cost()}[/]"
output += f"\n[yellow]car.insurance {car.insurance}[/]"
print("\n")
print(
    boxen(
        output,
        title="[blue]ORIGINAL VALUES[/]",  # closing tag can just be a '/'
        title_alignment="left",  # left center right
        subtitle="[blue]ORIGINAL VALUES[/blue]",
        subtitle_alignment="right",  # left center right
        color="blue",
        padding=1,
        fullwidth=True,  # sometimes does not seem to give full console width
    )
)
