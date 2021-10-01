# p26_1.py
class Animal:
    """動物"""
    def __init__(self, name):
        self.__name = name

    def running(self):
        print(self.__name + "在跑...")

Animal("貓").running()
Animal("狗").running()
