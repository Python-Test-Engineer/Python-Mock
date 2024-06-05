# program to create class dynamically
from pyboxen import boxen
from rich.console import Console

console = Console()


# constructor
def constructor(self, arg):
    self.constructor_arg = arg


# method
def displayMethod(self, arg):
    console.print(arg)


# class method
@classmethod
def classMethod(cls, arg):
    console.print(arg)


# creating class dynamically
Geeks = type(
    "Geeks",
    (object,),
    {
        # constructor
        "__init__": constructor,
        # data members
        "string_attribute": "Geeks 4 geeks !",
        "int_attribute": 1706256,
        "mock_attribute": 1000,
        # member functions
        "my_func_args": displayMethod,  # built in
        "my_class_func": classMethod,
    },
)
# https://stackoverflow.com/questions/48487093/how-arguments-in-python-decorated-functions-work - func_arg
# creating objects
obj = Geeks("constructor argument")
print(obj.constructor_arg)
print(obj.string_attribute)
print(obj.int_attribute)
print("=================")
console.print(obj.mock_attribute)
print("=================")
obj.my_func_args("mock_arg")
Geeks.my_class_func("Class Dynamically Created !")
