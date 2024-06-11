# 0 program to create class dynamically
import sys
import module02
from pyboxen import boxen
from rich.console import Console

console = Console()


class TestDouble:

    def __init__(self, msg):
        self.constructor_arg = msg

    def mocked_say_hello(self):
        return self.constructor_arg


# creating objects

obj = TestDouble("[red bold]TestDouble VALUE[/red bold]")

print("\n")

original_id = str(id(sys.modules["module02"].say_hello))[-6:-1]
original_say_hello = sys.modules["module02"].say_hello(
    "[blue bold]original module02.say_hello()[/]"
)

# patch say_hello() to use obj.mocked_say_hello
sys.modules["module02"].say_hello = obj.mocked_say_hello
# sys.modules["module01"].say_hello = lambda: obj.mock_attribute
# original say_hello()
console.print("Original ID", original_id)
console.print("our original say_hello()..", original_say_hello)

# patched say_hello()
console.print("TestDouble ID", str(id(sys.modules["module02"].say_hello))[-6:-1])
console.print(
    "our TestDouble say_hello()..", sys.modules["module02"].say_hello(), "\n\n"
)


console.print(globals())
