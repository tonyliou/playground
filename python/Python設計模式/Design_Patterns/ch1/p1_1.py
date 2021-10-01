#p1_1.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class WaterHeater:
    """熱水器：戰勝寒冬的有利武器"""
    def __init__(self):
        self.__observers = []
        self.__temperature = 25
    def getTemperature(self):
        return self.__temperature
    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("當前溫度是：" + str(self.__temperature) + "℃")
        self.notifies()
    def addObserver(self, observer):
        self.__observers.append(observer)
    def notifies(self):
        for o in self.__observers:
            o.update(self)

class Observer(metaclass=ABCMeta):
    "洗澡模式和飲用模式的父類別"
    @abstractmethod
    def update(self, waterHeater):
        pass

class WashingMode(Observer):
    """該模式用於洗澡"""
    def update(self, waterHeater):
        if waterHeater.getTemperature() >= 50 and waterHeater.getTemperature() < 70:
            print("水已燒好！溫度正好，可以用來洗澡了。")

class DrinkingMode(Observer):
    """該模式用於飲用"""
    def update(self, waterHeater):
        if waterHeater.getTemperature() >= 100:
            print("水已燒開！可以用來飲用了。")

heater = WaterHeater()
washingObser = WashingMode()
drinkingObser = DrinkingMode()
heater.addObserver(washingObser)
heater.addObserver(drinkingObser)
heater.setTemperature(40)
heater.setTemperature(60)
heater.setTemperature(100)
