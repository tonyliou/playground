# p20_1.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class Template(metaclass=ABCMeta):
    """範本類別(抽象類別)"""
    @abstractmethod
    def stepOne(self):
        pass
    @abstractmethod
    def stepTwo(self):
        pass
    @abstractmethod
    def stepThree(self):
        pass
    def templateMethold(self):
        """範本方法"""
        self.stepOne()
        self.stepTwo()
        self.stepThree()

class TemplateImplA(Template):
    """範本實現類別A"""
    def stepOne(self):
        print("步驟一")
    def stepTwo(self):
        print("步驟二")
    def stepThree(self):
        print("步驟三")

class TemplateImplB(Template):
    """範本實現類別B"""
    def stepOne(self):
        print("Step one")
    def stepTwo(self):
        print("Step two")
    def stepThree(self):
        print("Step three")
