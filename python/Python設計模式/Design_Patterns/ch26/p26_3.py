# p26_3.py
class Animal:
    """動物"""
    def __init__(self, name):
        self.__name = name
    def running(self):
        print(self.__name + "在陸上跑...")
    def swimming(self):
        print(self.__name + "在水裡遊...")

Animal("狗").running()
Animal("魚").swimming()
