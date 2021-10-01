# p13_2.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class Target(metaclass=ABCMeta):
    """目標類別"""
    @abstractmethod
    def function(self):
        pass

class Adaptee:
    """源物件類別"""
    def speciaficFunction(self):
        print("被適配物件的特殊功能")

class Adapter(Adaptee, Target):
    """適配器別"""
    def function(self):
        print("進行功能的轉換")
