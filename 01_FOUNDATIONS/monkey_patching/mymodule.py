from pathlib import Path  # import class "Path"
import itertools as I  # import module "itertools" aliased as "I"
from functools import reduce  # import selected function "reduce"
from pyboxen import boxen

from rich.console import Console

console = Console()
GLOBALVAR = 1


def foo():
    import urllib  # import module urllib to local namespace

    LOCALVAR = 2
    print("=== locals ===")
    output = str(locals())

    print(
        boxen(
            output,
            title="=== locals ===",
            subtitle="=== locals ===",
            subtitle_alignment="left",
            color="purple4",
            padding=1,
        )
    )


if __name__ == "__main__":
    foo()

    console.print(globals())

    import mymodule

    globals()["mymodule"]
