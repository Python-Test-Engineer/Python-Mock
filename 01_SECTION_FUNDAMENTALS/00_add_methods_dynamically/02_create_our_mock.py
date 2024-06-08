# 0 program to create class dynamically
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


# when we write class Mock() Python uses type to create the class:

# Mock is name of class
# (object,) is bases inherited or classes inherited
# class_dict is dictionary of members - properties and methods

# The purpose of this is to show that we can add at run time attributes to Mock by using setattr().


# creating class dynamically
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
Mock.my_class_method("Class Dynamically Created !")
obj.my_lambda("hello")()
result = obj.lambda_square(10)()
console.print("result is ", result)


console.print(globals())

# add properties and methods dynamically to Mock

setattr(Mock, "model", "a new model")
console.print(f"Dynamically added property model is [green]{Mock.model}[/]\n")


def new_function():

    return "mocked function"


setattr(Mock, "dynamic_method", new_function)
output = Mock.dynamic_method()
console.print(f"output is [green bold]{output}[/]\n")


console.print(sys.modules["module01"])

sys.modules["module01"].say_hello()

# we now patch module01 in to return PATCHED via the lambda as an alternative way of using functions


def return_mock_attribute():
    return obj.mock_attribute


# sys.modules["module01"].say_hello = return_mock_attribute
sys.modules["module01"].say_hello = lambda: obj.mock_attribute

console.print("our patched say_hello()..", sys.modules["module01"].say_hello(), "\n\n")
