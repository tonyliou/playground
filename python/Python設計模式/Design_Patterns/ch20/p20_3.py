# p20_3.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class Shape(metaclass=ABCMeta):
    """形狀"""
    def __init__(self, color):
        self._color = color
    @abstractmethod
    def getShapeType(self):
        pass
    def getShapeInfo(self):
        return self._color.getColor() + "的" + self.getShapeType()

class Rectange(Shape):
    """矩形"""
    def __init__(self, color):
        super().__init__(color)
    def getShapeType(self):
        return "矩形"

class Ellipse(Shape):
    """橢圓"""
    def __init__(self, color):
        super().__init__(color)
    def getShapeType(self):
        return "橢圓"

class Color(metaclass=ABCMeta):
    """顏色"""
    @abstractmethod
    def getColor(self):
        pass

class Red(Color):
    """紅色"""
    def getColor(self):
        return "紅色"

class Green(Color):
    """綠色"""
    def getColor(self):
        return "綠色"

def testShap():
    redRect = Rectange(Red())
    print(redRect.getShapeInfo())
    greenRect = Rectange(Green())
    print(greenRect.getShapeInfo())

    redEllipse = Ellipse(Red())
    print(redEllipse.getShapeInfo())
    greenEllipse = Ellipse(Green())
    print(greenEllipse.getShapeInfo())

testShap()
