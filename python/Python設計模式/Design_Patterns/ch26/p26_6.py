# p26_6.py

from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class Animal(metaclass=ABCMeta):
    """動物"""
    def __init__(self, name):
        self._name = name
    @abstractmethod
    def moving(self):
        pass

class TerrestrialAnimal(Animal):
    """陸生生物"""
    def __init__(self, name):
        super().__init__(name)
    def moving(self):
        print(self._name + "在陸上跑...")

class AquaticAnimal(Animal):
    """水生生物"""
    def __init__(self, name):
        super().__init__(name)
    def moving(self):
        print(self._name + "在水裡遊...")

class BirdAnimal(Animal):
    """鳥類動物"""
    def __init__(self, name):
        super().__init__(name)
    def moving(self):
        print(self._name + "在天空飛...")

class Zoo:
    """動物園"""
    def __init__(self):
        self.__animals =[]
    def addAnimal(self, animal):
        self.__animals.append(animal)
    def displayActivity(self):
        print("觀察每一種動物的活動方式：")
        for animal in self.__animals:
            animal.moving()

def testZoo():
    zoo = Zoo()
    zoo.addAnimal(TerrestrialAnimal("狗"))
    zoo.addAnimal(AquaticAnimal("魚"))
    zoo.addAnimal(BirdAnimal("鳥"))
    zoo.displayActivity()

testZoo()
