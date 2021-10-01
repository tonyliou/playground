# p21_2.py
def testFilter():
    rawMaterials = ["豆漿", "豆渣"]
    print("過濾前：", rawMaterials)
    filteredMaterials = list(filter(lambda material: material == "豆漿", rawMaterials))
    print("過濾後：", filteredMaterials)
