https://docs.python.org/3/library/unittest.mock.html#where-to-patch

Imagine we have a project that we want to test with the following structure:
```
a.py
    -> Defines SomeClass

b.py
    -> from a import SomeClass
    -> some_function instantiates SomeClass
```
Now we want to test some_function but we want to mock out SomeClass using patch(). The problem is that when we import module b, which we will have to do then it imports SomeClass from module a. 

If we use patch() to mock out a.SomeClass then it will have no effect on our test; module b already has a reference to the real SomeClass and it looks like our patching had no effect.