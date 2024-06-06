from pyboxen import boxen
from rich.console import Console

console = Console()

CONST_INT = 10


def say_hello():

    output = "Hello from module01.py"
    print("\n")
    print(
        boxen(
            output,
            title="[blue]module01 -> say_hello()[/]",  # closing tag can just be a '/'
            title_alignment="center",  # left center right
            subtitle="[blue]module01 -> say_hello()S[/blue]",
            subtitle_alignment="center",  # left center right
            color="green",
            padding=1,
            fullwidth=True,  # sometimes does not seem to give full console width
        )
    )


if __name__ == "__main__":
    say_hello()
