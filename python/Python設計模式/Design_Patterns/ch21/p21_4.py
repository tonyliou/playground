# p21_4.py
from p21_3 import Filter

class FilterScreen(Filter):
    """過濾網"""
    def doFilter(self, elements):
        for material in elements:
            if (material == "豆渣"):
                elements.remove(material)
        return elements
