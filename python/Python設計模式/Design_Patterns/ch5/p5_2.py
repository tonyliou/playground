# p5_2.py
class Singleton1(object):
    """單例實現方式一"""
    __instance = None
    __isFirstInit = False
    def __new__(cls, name):
        if not cls.__instance:
            Singleton1.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            Singleton1.__isFirstInit = True
    def getName(self):
        return self.__name

# Test
tony = Singleton1("Tony")
karry = Singleton1("Karry")
print(tony.getName(), karry.getName())
print("id(tony):", id(tony), "id(karry):", id(karry))
print("tony == karry:", tony == karry)
