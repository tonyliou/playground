# pb_4.py

class Sample:
    def __str__(self):
        return "SAMPLE"

class ClassB:
    def __new__(cls):
        print("ClassB.__new__")
        return super().__new__(Sample)
        # return Sample() # 也可以用這種寫法
    def __init__(self):
        print("ClassB.__init__")

b = ClassB()
print(b)
print(type(b))
