# p15_1.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class Coffee(metaclass=ABCMeta):
    """咖啡"""
    def __init__(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    @abstractmethod
    def getTaste(self):
        pass

class LatteCaffe(Coffee):
    """拿鐵咖啡"""
    def __init__(self, name):
        super().__init__(name)
    def getTaste(self):
        return "輕柔而香醇"

class MochaCoffee(Coffee):
    """摩卡咖啡"""
    def __init__(self, name):
        super().__init__(name)
    def getTaste(self):
        return "絲滑與醇厚"

class Coffeemaker:
    """咖啡機"""
    @staticmethod
    def makeCoffee(coffeeBean):
        "通過staticmethod裝飾器修飾來定義一個靜態方法"
        if(coffeeBean == "拿鐵咖啡豆"):
            coffee = LatteCaffe("拿鐵咖啡")
        elif(coffeeBean == "摩卡咖啡豆"):
            coffee = MochaCoffee("摩卡咖啡")
        else:
            raise ValueError("不支持的參數：%s" % coffeeBean)
        return coffee

def testCoffeeMaker():
    latte = Coffeemaker.makeCoffee("拿鐵咖啡豆")
    print("%s已為您準備好了，口感：%s。請慢慢享用！" % (latte.getName(), latte.getTaste()) )
    mocha = Coffeemaker.makeCoffee("摩卡咖啡豆")
    print("%s已為您準備好了，口感：%s。請慢慢享用！" % (mocha.getName(), mocha.getTaste()))

testCoffeeMaker()

