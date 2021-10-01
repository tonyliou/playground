# p14_1.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class IVehicle(metaclass=ABCMeta):
    """交通工具的抽象類別"""
    @abstractmethod
    def running(self):
        pass

class SharedBicycle(IVehicle):
    """共用單車"""
    def running(self):
        print("騎共用單車(輕快便捷)", end='')

class ExpressBus(IVehicle):
    """快速公交"""
    def running(self):
        print("坐快速公交(經濟綠色)", end='')

class Express(IVehicle):
    """快車"""
    def running(self):
        print("打快車(快速方便)", end='')

class Subway(IVehicle):
    """地鐵"""
    def running(self):
        print("坐地鐵(高效安全)", end='')

class Classmate:
    """來聚餐的同學"""
    def __init__(self, name, vechicle):
        self.__name = name
        self.__vechicle = vechicle
    def attendTheDinner(self):
        print(self.__name + " ", end='')
        self.__vechicle.running()
        print(" 來聚餐！")

def testTheDinner():
    sharedBicycle = SharedBicycle()
    joe = Classmate("Joe", sharedBicycle)
    joe.attendTheDinner()
    helen = Classmate("Helen", Subway())
    helen.attendTheDinner()
    henry = Classmate("Henry", ExpressBus())
    henry.attendTheDinner()
    ruby = Classmate("Ruby", Express())
    ruby.attendTheDinner()

testTheDinner()
