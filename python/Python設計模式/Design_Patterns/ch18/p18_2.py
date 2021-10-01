# p18_2.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class Flyweight(metaclass=ABCMeta):
    """享元類別"""
    @abstractmethod
    def operation(self, extrinsicState):
        pass

class FlyweightImpl(Flyweight):
    """享元類的具體實現類別"""
    def __init__(self, color):
        self.__color = color
    def operation(self, extrinsicState):
        print("%s 取得 %s色顏料" % (extrinsicState, self.__color))

class FlyweightFactory:
    """享元工廠"""
    def __init__(self):
       self.__flyweights = {}
    def getFlyweight(self, key):
        pigment = self.__flyweights.get(key)
        if pigment is None:
            pigment = FlyweightImpl(key)
        return pigment

def testFlyweight():
    factory = FlyweightFactory()
    pigmentRed = factory.getFlyweight("紅")
    pigmentRed.operation("夢之隊")
    pigmentYellow = factory.getFlyweight("黃")
    pigmentYellow.operation("夢之隊")
    pigmentBlue1 = factory.getFlyweight("藍")
    pigmentBlue1.operation("夢之隊")
    pigmentBlue2 = factory.getFlyweight("藍")
    pigmentBlue2.operation("和平隊")

testFlyweight()
