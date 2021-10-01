# pb_1.py
class ClassA:
    def __new__(cls):
        print("ClassA.__new__")
        return super().__new__(cls)
    def __init__(self):
        print("ClassA.__init__")
    def __call__(self, *args):
        print("ClassA.__call__ args:", args)

a = ClassA()
a("arg1", "arg2")
