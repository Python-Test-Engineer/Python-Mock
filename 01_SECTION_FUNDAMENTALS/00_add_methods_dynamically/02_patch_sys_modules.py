# program to create class dynamically
import sys
import module02

from rich.console import Console

console = Console()

console.print(globals())

console.print(sys.modules)
console.print(sys.modules["module02"])

console.print("\n[blue]we can run say_hello() now from sys.modules[/]\n")

# we can get the memory address, or id, of an object using id()
# we will display the last 5 digits...
console.print("Original ID", str(id(sys.modules["module02"].say_hello))[-6:-1])

# we can reference the object in sys.modules and call the say_hello()
original_say_hello = sys.modules["module02"].say_hello("ORIGINAL say_hello()")
console.print("[yellow]our ORIGINAL say_hello() is now =>[/]", original_say_hello)


# we now patch module01 in to return PATCHED by redirecting it to say_hello_patched()
def say_hello_patched():
    return "DEF PATCHED"


# sys.modules["module02"].say_hello = say_hello_patched
sys.modules["module02"].say_hello = lambda: "LAMBDA PATCHED"

# we can see the id of say_hello() has changed
console.print("\nPatched ID", str(id(sys.modules["module02"].say_hello))[-6:-1])

# when we call the patched version we now get...
console.print(
    "[green]our patched say_hello() is now =>[/]",
    sys.modules["module02"].say_hello(),
    "\n\n",
)
