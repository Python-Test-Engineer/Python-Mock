# program to create class dynamically
import sys
import module01
from pyboxen import boxen
from rich.console import Console

console = Console()


console.print(globals())

console.print(sys.modules["module01"])

sys.modules["module01"].say_hello()


# we now patch module01 in to return PATCHED
def say_hello():
    return "DEF PATCHED"


sys.modules["module01"].say_hello = say_hello
# sys.modules["module01"].say_hello = lambda: "LAMBDA PATCHED"

console.print(
    "[green]our patched say_hello() =>[/]", sys.modules["module01"].say_hello(), "\n\n"
)
