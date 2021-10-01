# p6_4.py
from copy import copy, deepcopy

class Clone:
    """克隆的基類別"""
    def clone(self):
        """淺拷貝的方式克隆物件"""
        return copy(self)
    def deepClone(self):
        """深拷貝的方式克隆物件"""
        return deepcopy(self)
