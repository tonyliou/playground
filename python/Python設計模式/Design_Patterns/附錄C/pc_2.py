# pc_2.py
ClassVariable = type('ClassA', (object,), dict(name="type test"))
a = ClassVariable()
print(type(a))
print(a.name)
