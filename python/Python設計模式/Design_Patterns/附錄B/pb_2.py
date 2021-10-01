# pb_2.py
class ClassB:
    def __new__(cls):
        print("ClassB.__new__")
        # return super().__new__(cls)
    def __init__(self):
        print("ClassB.__init__")

b = ClassB()
print(b)
