# program to create class dynamically
import sys
import module02
from rich.console import Console

console = Console()


class Mock:

    def __init__(self, msg):
        self.constructor_arg = msg

    def mocked_say_hello(self):
        return self.constructor_arg


# creating objects

m = Mock("PATCHED")

print("\n")

original_id = str(id(sys.modules["module02"].say_hello))[-6:-1]
original_say_hello = sys.modules["module02"].say_hello(
    "[blue bold]original module02.say_hello()[/]"
)


def dynamic_mock_method():
    dynamic_mock_attribute = "[yellow bold]DYNAMICALLY MOCKED ATTRIUBUTE[/]"
    return dynamic_mock_attribute


# we don't have to add it as an instance method but can add it to class.

# m.mocked_say_hello = dynamic_mock_method
# we can add ot instance at run time if we want to
setattr(m, "mocked_say_hello", dynamic_mock_method)


# patch say_hello() to use return_mock_attribute
sys.modules["module02"].say_hello = m.mocked_say_hello
# original say_hello()
console.print("ORIGINAL ID", original_id)
console.print("our original say_hello()...", original_say_hello)

# patched say_hello()
console.print("MOCKED ID", str(id(sys.modules["module02"].say_hello))[-6:-1])
console.print("our mocked say_hello()...", sys.modules["module02"].say_hello(), "\n\n")
