# p21_1.py
class FilterScreen:
    """過濾網"""
    def doFilter(self, rawMaterials):
        for material in rawMaterials:
            if (material == "豆渣"):
                rawMaterials.remove(material)
        return rawMaterials

def testFilterScreen():
    rawMaterials = ["豆漿", "豆渣"]
    print("過濾前：", rawMaterials)
    filter = FilterScreen()
    filteredMaterials = filter.doFilter(rawMaterials)
    print("過濾後：", filteredMaterials)

testFilterScreen()
