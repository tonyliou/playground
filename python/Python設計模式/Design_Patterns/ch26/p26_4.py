# p26_4.py
class TerrestrialAnimal():
    """陸生生物"""
    def __init__(self, name):
        self.__name = name
    def running(self):
        print(self.__name + "在陸上跑...")

class AquaticAnimal():
    """水生生物"""
    def __init__(self, name):
        self.__name = name
    def swimming(self):
        print(self.__name + "在水裡遊...")

TerrestrialAnimal("狗").running()
AquaticAnimal("魚").swimming()
