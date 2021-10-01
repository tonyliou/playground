# p5_4.py
def singletonDecorator(cls, *args, **kwargs):
    """定義一個單例裝飾器"""
    instance = {}
    def wrapperSingleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapperSingleton

@singletonDecorator
class Singleton3:
    """使用單例裝飾器修飾一個類"""
    def __init__(self, name):
        self.__name = name
    def getName(self):
        return self.__name

tony = Singleton3("Tony")
karry = Singleton3("Karry")
print(tony.getName(), karry.getName())
print("id(tony):", id(tony), "id(karry):", id(karry))
print("tony == karry:", tony == karry)

