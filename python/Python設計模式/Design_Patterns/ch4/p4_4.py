# p4_4.py
class ClassDecorator:
    """類裝飾器，記錄一個類被產生實體的次數"""

    def __init__(self, func):
        self.__numOfCall = 0
        self.__func = func

    def __call__(self, *args, **kwargs):
        self.__numOfCall += 1
        obj = self.__func(*args, *kwargs)
        print("創建%s的第%d個實例:%s" % (self.__func.__name__, self.__numOfCall, id(obj)))
        return obj

@ClassDecorator
class MyClass:

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


tony = MyClass("Tony")
karry = MyClass("Karry")
print(id(tony))
print(id(karry))

