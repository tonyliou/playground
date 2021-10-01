# pc_5.py
from pc_4 import SubClass, BaseClass

print(issubclass(SubClass, BaseClass))
print(issubclass(BaseClass, SubClass))
print(SubClass.__bases__)
