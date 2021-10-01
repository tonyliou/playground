# pc_7.py
class CustomMetaclass(type):
    pass

class CustomClass(metaclass=CustomMetaclass):
    pass

print(type(object))
print(type(type))
print()

obj = CustomClass()
print(type(CustomClass))
print(type(obj))

print()
print(isinstance(obj, CustomClass))
print(isinstance(obj, object))
