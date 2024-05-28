https://github.com/python/cpython/blob/main/Lib/unittest/mock.py


https://mgarod.medium.com/dynamically-add-a-method-to-a-class-in-python-c49204b85bd6




https://igorsobreira.com/2011/02/06/adding-methods-dynamically-in-python.html

Adding methods dynamically in Python
Feb 6, 2011

Given the dynamic nature of Python you can do many things in runtime, like add methods dynamically to an object or class. This is particularly useful when writing unit tests.

Here is the simplest way, adding a method to and object:
```
class Person(object):
    pass

def play():
    print "i'm playing!"

p = Person()
p.play = play
p.play()
```
note that play is just a function, it doesn’t receive self. There is no way to p knows that it’s a method. If you need self, you must create a method and then bind to the object:
```
from types import MethodType

class Person(object):
    def __init__(self, name):
        self.name = name

def play(self):
    print "%s is playing!" % self.name

p = Person("igor")
p.play = MethodType(play, p)
p.play()

```
In these examples, only the p instance will have play method, other instances of Person won’t. To accomplish this we need to add the method to the class:
```
class Person(object):
    def __init__(self, name):
        self.name = name

def play(self):
    print "%s is playing!" % self.name

Person.play = play

p1 = Person("igor")
p1.play()

p2 = Person("joh")
p2.play()
```
note that we don’t need to create a method with types.MethodType here, because all functions in the body of a class will become methods and receive self, unless you explicit say it’s a classmethod or staticmethod.