# program to create class dynamically
import sys
import module02

from rich.console import Console

console = Console()

# console.print(globals())

# console.print(sys.modules)
console.print(sys.modules["module02"])

console.print("\n[blue]we can run say_hello() now from sys.modules[/]\n")

console.print("Original ID", str(id(sys.modules["module02"].say_hello))[-6:-1])
original_say_hello = sys.modules["module02"].say_hello("ORIGINAL say_hello()")
console.print("[yellow]our ORIGINAL say_hello() is now =>[/]", original_say_hello)


# we now patch module01 in to return PATCHED
def say_hello_patched():
    return "DEF PATCHED"


sys.modules["module02"].say_hello = say_hello_patched
# sys.modules["module01"].say_hello = lambda: "LAMBDA PATCHED"

console.print("\nPatched ID", str(id(sys.modules["module02"].say_hello))[-6:-1])
console.print(
    "[green]our patched say_hello() is now =>[/]",
    sys.modules["module02"].say_hello(),
    "\n\n",
)
