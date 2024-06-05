https://stackoverflow.com/questions/2954331/dynamically-adding-property-in-python

```
ef addprop(inst, name, method):
  cls = type(inst)
  if not hasattr(cls, '__perinstance'):
    cls = type(cls.__name__, (cls,), {})
    cls.__perinstance = True
    inst.__class__ = cls
  setattr(cls, name, property(method))
```

https://stackoverflow.com/questions/75050310/python-dynamically-add-properties-to-class-instance-properties-return-function
```
class Value_Differences():
    def __init__(self, parent : Evolution_Base, property_list = []):
        self._parent = parent
        self._property_list = property_list

    def __dir__(self):
        return sorted(set(
               dir(super(Value_Differences, self)) + \
               list(self.__dict__.keys()) + self._property_list))

    def __getattr__(self, __name: str):
        if __name in self._property_list:
            return self._parent._get_df_change(__name)
class Value_Differences():
    def __init__(self, parent : Evolution_Base, property_list = []):
        self._parent = parent
        self._property_list = property_list

    def __dir__(self):
        return sorted(set(
               dir(super(Value_Differences, self)) + \
               list(self.__dict__.keys()) + self._property_list))

    def __getattr__(self, __name: str):
        if __name in self._property_list:
            return self._parent._get_df_change(__name)class Value_Differences():
    def __init__(self, parent : Evolution_Base, property_list = []):
        self._parent = parent
        self._property_list = property_list

    def __dir__(self):
        return sorted(set(
               dir(super(Value_Differences, self)) + \
               list(self.__dict__.keys()) + self._property_list))

    def __getattr__(self, __name: str):
        if __name in self._property_list:
            return self._parent._get_df_change(__name)class Value_Differences():
    def __init__(self, parent : Evolution_Base, property_list = []):
        self._parent = parent
        self._property_list = property_list

    def __dir__(self):
        return sorted(set(
               dir(super(Value_Differences, self)) + \
               list(self.__dict__.keys()) + self._property_list))

    def __getattr__(self, __name: str):
        if __name in self._property_list:
            return self._parent._get_df_change(__name)
```

https://www.geeksforgeeks.org/create-classes-dynamically-in-python/

```
# program to create class dynamically 

# constructor 
def constructor(self, arg): 
	self.constructor_arg = arg 

# method 
def displayMethod(self, arg): 
	print(arg) 

# class method 
@classmethod
def classMethod(cls, arg): 
	print(arg) 

# creating class dynamically 
Geeks = type("Geeks", (object, ), { 
	# constructor 
	"__init__": constructor, 
	
	# data members 
	"string_attribute": "Geeks 4 geeks !", 
	"int_attribute": 1706256, 
	
	# member functions 
	"func_arg": displayMethod, 
	"class_func": classMethod
}) 

# creating objects 
obj = Geeks("constructor argument") 
print(obj.constructor_arg) 
print(obj.string_attribute) 
print(obj.int_attribute) 
obj.func_arg("Geeks for Geeks") 
Geeks.class_func("Class Dynamically Created !") 
```