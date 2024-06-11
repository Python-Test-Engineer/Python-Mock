# We can use a the class within its class definition.abs

# This shows how a Mock can return Mock object.

# This is important to know because it explains how creating a Mock and adding methods and properties to it, also returns a Mock object.

from rich.console import Console

console = Console()


class Mock(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f"Hi, I am {self.name}. I am {self.age} years old."

    def family(self):

        return [Mock("Adam", 25), Mock("Eve", 22)]

    def __str__(self):
        return "Mock({self.name}, {self.age})"


if __name__ == "__main__":
    m = Mock("John", 30)
    print(m.greeting())
    family = m.family()
    for i in family:
        print(i.greeting())
    console.print(
        "\n[yellow italic]add a property dynamically to Mock at run time...[/]"
    )
    if 2 == 3:
        setattr(Mock, "language", "Python")
        console.print(f"Mocked property model is [green]{Mock.language}[/]\n")
