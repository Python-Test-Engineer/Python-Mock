# This is important to know because it explains how creating a Mock and adding methods and properties to it, also returns a Mock object.

# See 02_python_mock_examples tests

# python .\01_FOUNDATIONS\01_our_mock\class_using_class.py


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f"Hi, I am {self.name}. I am {self.age} years old."

    def family(self):

        return [Person("Adam", 25), Person("Eve", 22)]

    def __str__(self):
        return "Person({}, {})".format(self.name, self.age)


if __name__ == "__main__":
    person = Person("John", 30)
    print(person.greeting())
    family = person.family()
    for i in family:
        print(i.greeting())
