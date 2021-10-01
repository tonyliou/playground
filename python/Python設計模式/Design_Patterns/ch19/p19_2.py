# p19_2.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class DataNode(metaclass=ABCMeta):
    """資料結構類別"""
    def accept(self, visitor):
        """接受訪問者的訪問"""
        visitor.visit(self)

class Visitor(metaclass=ABCMeta):
    """訪問者"""
    @abstractmethod
    def visit(self, data):
        """對資料物件的訪問操作"""
        pass

class ObjectStructure:
    """資料結構的管理類別，也是資料物件的一個容器，可遍歷容器內的所有元素"""
    def __init__(self):
        self.__datas = []
    def add(self, dataElement):
        self.__datas.append(dataElement)
    def action(self, visitor):
        """進行資料訪問的操作"""
        for data in self.__datas:
            data.accept(visitor)
