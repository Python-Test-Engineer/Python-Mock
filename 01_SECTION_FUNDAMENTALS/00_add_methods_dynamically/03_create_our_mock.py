# 0 program to create class dynamically
import sys
import module02
from pyboxen import boxen
from rich.console import Console

console = Console()


# constructor
def my_constructor(self, arg):
    self.constructor_arg = arg


# method
def my_displayMethod(self, arg):
    console.print(arg)


# class method
@classmethod
def my_classMethod(cls, arg):
    console.print(arg)


# creating class with type before compiling or dynamically at run time.
Mock = type(
    "Mock",  # name
    (object,),  # inheritance of base object
    {
        # constructor
        "__init__": my_constructor,
        # data members
        "string_attribute": "Our first mock",
        "int_attribute": 1706256,
        "mock_attribute": "PATCHED dynamically added attribute",
        # member functions
        "my_func_args": my_displayMethod,  # built in
        "my_class_method": my_classMethod,
        "my_lambda": lambda self, arg: lambda: console.print(arg),
        "lambda_square": lambda self, x: lambda: x * x,
    },
)


# creating objects
obj = Mock("constructor argument")

print("\n")

original_id = str(id(sys.modules["module02"].say_hello))[-6:-1]
original_say_hello = sys.modules["module02"].say_hello("original say_hello()")


# create a new function
def new_function():

    return "mocked function"


# # let's patch module01
# # current say_hello() function is stored in sys.modules["module01"]
# console.print(sys.modules["module01"])

# sys.modules["module02"].say_hello("original say_hello()")


# we now patch module01.say_hello() to return PATCHED via the function return_mock_attribute and we can use a lambda as an alternative way of using functions
# mock_attribute": "PATCHED dynamically added attribute",
def return_mock_attribute():
    return obj.mock_attribute


# patch say_hello() to use return_mock_attribute
sys.modules["module02"].say_hello = return_mock_attribute
# sys.modules["module01"].say_hello = lambda: obj.mock_attribute
# original say_hello()
console.print("Patched ID", original_id)
console.print("our original say_hello()..", original_say_hello)

# patched say_hello()
console.print("Patched ID", str(id(sys.modules["module02"].say_hello))[-6:-1])
console.print("our patched say_hello()..", sys.modules["module02"].say_hello(), "\n\n")


# console.print(globals())
