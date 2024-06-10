# 0 program to create class dynamically
import sys
import module02
from pyboxen import boxen
from rich.console import Console

console = Console()


class Mock(object):

    def __init__(self, msg):
        self.constructor_arg = msg

    def mocked_say_hello(self):
        return self.constructor_arg


# creating objects

obj = Mock("PATCHED")

print("\n")

original_id = str(id(sys.modules["module02"].say_hello))[-6:-1]
original_say_hello = sys.modules["module02"].say_hello(
    "[blue bold]original module02.say_hello()[/]"
)


# # let's patch module02
# # current say_hello() function is stored in sys.modules["module02"]
# console.print(sys.modules["module02"])


def return_mock_attribute():
    return "[yellow bold]MOCKED[/yellow bold]"


obj.mocked_say_hello = return_mock_attribute
# patch say_hello() to use return_mock_attribute
sys.modules["module02"].say_hello = obj.mocked_say_hello
# sys.modules["module01"].say_hello = lambda: obj.mock_attribute
# original say_hello()
console.print("Patched ID", original_id)
console.print("our original say_hello()..", original_say_hello)

# patched say_hello()
console.print("Patched ID", str(id(sys.modules["module02"].say_hello))[-6:-1])
console.print("our patched say_hello()..", sys.modules["module02"].say_hello(), "\n\n")


# console.print(globals())
