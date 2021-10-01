# p11_2.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class Component(metaclass=ABCMeta):
    """組件"""
    def __init__(self, name):
        self._name = name
    def getName(self):
        return self._name
    def isComposite(self):
        return False
    @abstractmethod
    def feature(self, indent):
        # indent 僅用於內容輸出時的縮進
        pass

class Composite(Component):
    """複合組件"""
    def __init__(self, name):
        super().__init__(name)
        self._components = []
    def addComponent(self, component):
        self._components.append(component)
    def removeComponent(self, component):
        self._components.remove(component)
    def isComposite(self):
        return True
    def feature(self, indent):
        indent += "\t"
        for component in self._components:
            print(indent, end="")
            component.feature(indent)
