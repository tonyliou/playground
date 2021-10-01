# pc_4.py
class BaseClass:
    name = "Base"

class SubClass(BaseClass):
    pass

base = BaseClass()
sub = SubClass()
print(isinstance(base, BaseClass))
print(isinstance(base, SubClass))
print()
print(isinstance(sub, SubClass))
print(isinstance(sub, BaseClass))
