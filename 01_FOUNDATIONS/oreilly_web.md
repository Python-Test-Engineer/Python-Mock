
https://www.oreilly.com/library/view/python-cookbook/0596001673/ch05s13.html

Adding Methods to a Class at Runtime
Credit: Brett Cannon

Problem
You want to add a method to a class at an arbitrary point in your code for highly dynamic customization.

Solution
The best way to perform this task works for both classic and new-style classes:

def funcToMethod(func, clas, method_name=None):
    setattr(clas, method_name or func._ _name_ _, func)
If a method of the specified name already exists in the class, funcToMethod replaces it with the new implementation.

Discussion
Ruby can add a method to a class at an arbitrary point in your code. I figured Python must have a way for allowing this to happen, and it turned out it did. There are several minor possible variations, but this recipe is very direct and compact, and works for both classic and new-style classes. The method just added is available instantly to all existing instances and to those not yet created. If you specify method_name, that name is used as the method name; otherwise, the method name is the same as the name of the function.

You can use this recipe for highly dynamic customization of a running program. On command, you can load a function from a module and install it as a method of a class (even in place of another previous implementation), thus instantly changing the behavior of all existing and new instances of the class.

One thing to make sure of is that the function has a first argument for the instance that will be passed to it (which is, conventionally, always named self). Also, this approach works only if func is a Python function, not a built-in or callable. For example, a built-in such as math.sin can be installed with this recipe’s funcToMethod function. However, it doesn’t turn into a method; it remains exactly the same, regardless of whether you access it as an attribute of a class or of an instance. Only true Python functions implicitly mutate into methods (bound or unbound as appropriate) when installed and accessed this way.

For classic classes, you can use a different approach for installing a callable as a method of a class:
```
def callableToMethod(func, clas, method_name=None):
    import new
    method = new.instancemethod(func, None, clas)
    setattr(clas, method_name or func._ _name_ _, method)
```
Now func can be any callable, such as an instance of any class that supplies a _ _call_ _ special method, a built-in, or a bound method.

The name of the instancemethod function of the new module may be slightly misleading. The function generates both bound and unbound methods, depending on whether the second argument is None (unbound) or an instance of the class that is the third argument. This function, however, works only with classic classes, not with new-style classes. See http://www.python.org/doc/current/lib/module-new.html for all the details (there’s not much more to it than this, though).