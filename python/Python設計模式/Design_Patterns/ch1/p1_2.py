#p1_2.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法
class Observer(metaclass=ABCMeta):
    """觀察者的基類別"""
    @abstractmethod
    def update(self, observable, object):
        pass

class Observable:
    """被觀察者的基類別"""
    def __init__(self):
        self.__observers = []
    def addObserver(self, observer):
        self.__observers.append(observer)
    def removeObserver(self, observer):
        self.__observers.remove(observer)
    def notifyObservers(self, object=0):
        for o in self.__observers:
            o.update(self, object)

