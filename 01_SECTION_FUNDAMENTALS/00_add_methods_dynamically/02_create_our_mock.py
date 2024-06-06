# program to create class dynamically
import sys
import module01
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


# creating class dynamically
Mock = type(
    "Mock",  # name
    (object,),  # inheritance of bases
    {
        # constructor
        "__init__": my_constructor,
        # data members
        "string_attribute": "Our first mock",
        "int_attribute": 1706256,
        "mock_attribute": "a patched attribute",
        # member functions
        "my_func_args": my_displayMethod,  # built in
        "my_class_func": my_classMethod,
        "my_lambda": lambda self, arg: lambda: console.print(arg),
        "lambda_square": lambda self, x: lambda: x * x,
    },
)
# https://stackoverflow.com/questions/48487093/how-arguments-in-python-decorated-functions-work - func_arg

# creating objects
obj = Mock("constructor argument")
print("\n")
console.print(obj.constructor_arg)
console.print(obj.string_attribute)
console.print(obj.int_attribute)
print("\n======= obj.mock_attribute =======")
console.print("\t", obj.mock_attribute)
print("======= obj.mock_attribute =======\n")
obj.my_func_args("mock_arg")
Mock.my_class_func("Class Dynamically Created !")
obj.my_lambda("hello")()
result = obj.lambda_square(10)()
console.print("result is ", result)

# console.print(globals())

# console.print(sys.modules["module01"])

# sys.modules["module01"].say_hello()

# # we now patch module01 in to return PATCHED

# sys.modules["module01"].say_hello = lambda: obj.mock_attribute

# console.print("our patched say_hello()..", sys.modules["module01"].say_hello(), "\n\n")
