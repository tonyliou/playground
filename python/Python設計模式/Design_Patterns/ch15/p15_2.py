# p15_2.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法
from enum import Enum
# Python 3.4之後支援枚舉Enum的語法

class PenType(Enum):
    """畫筆類別型"""
    PenTypeLine = 1
    PenTypeRect = 2
    PenTypeEllipse = 3


class Pen(metaclass=ABCMeta):
    """畫筆"""
    def __init__(self, name):
        self.__name = name
    @abstractmethod
    def getType(self):
        pass
    def getName(self):
        return self.__name

class LinePen(Pen):
    """直線畫筆"""
    def __init__(self, name):
        super().__init__(name)
    def getType(self):
        return PenType.PenTypeLine

class RectanglePen(Pen):
    """矩形畫筆"""
    def __init__(self, name):
        super().__init__(name)
    def getType(self):
        return PenType.PenTypeRect

class EllipsePen(Pen):
    """橢圓畫筆"""
    def __init__(self, name):
        super().__init__(name)
    def getType(self):
        return PenType.PenTypeEllipse

class PenFactory:
    """畫筆工廠類別"""
    def __init__(self):
        "定義一個字典(key:PenType，value：Pen)來存放物件,確保每一個類別型只會有一個物件"
        self.__pens = {}
    def getSingleObj(self, penType, name):
        """獲得唯一實例的物件"""
    def createPen(self, penType):
        """創建畫筆"""
        if (self.__pens.get(penType) is None):
            # 如果該物件不存在，則創建一個物件並存到字典中
            if penType == PenType.PenTypeLine:
                pen = LinePen("直線畫筆")
            elif penType == PenType.PenTypeRect:
                pen = RectanglePen("矩形畫筆")
            elif penType == PenType.PenTypeEllipse:
                pen = EllipsePen("橢圓畫筆")
            else:
                pen = Pen("")
            self.__pens[penType] = pen
        # 否則直接返回字典中的物件
        return self.__pens[penType]

def testPenFactory():
    factory = PenFactory()
    linePen = factory.createPen(PenType.PenTypeLine)
    print("創建了 %s，物件id：%s， 類別：%s" % (linePen.getName(), id(linePen), linePen.getType()) )
    rectPen = factory.createPen(PenType.PenTypeRect)
    print("創建了 %s，物件id：%s， 類別：%s" % (rectPen.getName(), id(rectPen), rectPen.getType()) )
    rectPen2 = factory.createPen(PenType.PenTypeRect)
    print("創建了 %s，物件id：%s， 類別：%s" % (rectPen2.getName(), id(rectPen2), rectPen2.getType()) )
    ellipsePen = factory.createPen(PenType.PenTypeEllipse)
    print("創建了 %s，物件id：%s， 類別：%s" % (ellipsePen.getName(), id(ellipsePen), ellipsePen.getType()) )

testPenFactory()

