# p1_3.py
from abc import ABCMeta, abstractmethod
from p1_2 import Observer, Observable
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class WaterHeater(Observable):
    """熱水器：戰勝寒冬的有力武器"""
    def __init__(self):
        super().__init__()
        self.__temperature = 25
    def getTemperature(self):
        return self.__temperature
    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("當前溫度是：" + str(self.__temperature) + "℃")
        self.notifyObservers()

class WashingMode(Observer):
    """該模式用於洗澡"""
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) \
                and observable.getTemperature() >= 50 and observable.getTemperature() < 70:
            print("水已燒好！溫度正好，可以用來洗澡了。")

class DrinkingMode(Observer):
    "該模式用於飲用"
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
            print("水已燒開！可以用來飲用了。")

heater = WaterHeater()
washingObser = WashingMode()
drinkingObser = DrinkingMode()
heater.addObserver(washingObser)
heater.addObserver(drinkingObser)
heater.setTemperature(40)
heater.setTemperature(60)
heater.setTemperature(100)

