# pb_3.py
class ClassB:
    def __new__(cls):
        print("ClassB.__new__")
        return 3.0
    def __init__(self):
        print("ClassB.__init__")

b = ClassB()
print(b)
