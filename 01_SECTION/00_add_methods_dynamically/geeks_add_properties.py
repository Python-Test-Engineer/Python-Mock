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
Mock = type(
    "Mock",  # name
    (object,),  # inheritance of bases
    {
        # constructor
        "__init__": constructor,
        # data members
        "string_attribute": "Our first mock",
        "int_attribute": 1706256,
        "mock_attribute": 1000,
        # member functions
        "my_func_args": displayMethod,  # built in
        "my_class_func": classMethod,
        "my_lambda": lambda self, arg: lambda: console.print(arg),
        "lambda_square": lambda self, x: lambda: x * x,
    },
)
# https://stackoverflow.com/questions/48487093/how-arguments-in-python-decorated-functions-work - func_arg

# creating objects
obj = Mock("constructor argument")
console.print(obj.constructor_arg)
console.print(obj.string_attribute)
console.print(obj.int_attribute)
print("======= obj.mock_attribute =======")
console.print("\t\t", obj.mock_attribute)
print("======= obj.mock_attribute =======")
obj.my_func_args("mock_arg")
Mock.my_class_func("Class Dynamically Created !")
obj.my_lambda("hello")()
result = obj.lambda_square(10)()
console.print("result is ", result)
