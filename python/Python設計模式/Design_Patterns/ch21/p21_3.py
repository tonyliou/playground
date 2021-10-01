# p21_3.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class Filter(metaclass=ABCMeta):
    """篩檢程式"""
    @abstractmethod
    def doFilter(self, elements):
        """過濾方法"""
        pass

class FilterChain(Filter):
    """篩檢程式鏈"""
    def __init__(self):
        self._filters = []
    def addFilter(self, filter):
        self._filters.append(filter)
    def removeFilter(self, filter):
        self._filters.remove(filter)
    def doFilter(self, elements):
        for filter in self._filters:
            elements = filter.doFilter(elements)
        return elements
