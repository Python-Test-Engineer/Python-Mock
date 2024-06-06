# program to create class dynamically
import sys
import module01
from pyboxen import boxen
from rich.console import Console

console = Console()


# console.print(globals())

console.print(sys.modules["module01"])

console.print("[yellow]we can run say_hello() now from sys.modules[/]")
sys.modules["module01"].say_hello()
console.print("Original ID", str(id(sys.modules["module01"].say_hello))[-6:-1])


# we now patch module01 in to return PATCHED
def say_hello_patched():
    return "DEF PATCHED"


sys.modules["module01"].say_hello = say_hello_patched
# sys.modules["module01"].say_hello = lambda: "LAMBDA PATCHED"
console.print("Patched ID", str(id(sys.modules["module01"].say_hello))[-6:-1])

console.print(
    "[green]our patched say_hello() is now =>[/]",
    sys.modules["module01"].say_hello(),
    "\n\n",
)
