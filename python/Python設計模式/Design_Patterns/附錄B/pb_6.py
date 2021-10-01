# pb_6.py
class ClassC:
    def __init__(self, *args, **kwargs):
        print("init", args, kwargs)

    def __new__(cls, *args, **kwargs):
        print("new", args, kwargs)
        return super().__new__(cls)

c = ClassC("arg1", "arg2", a=1, b=2)
