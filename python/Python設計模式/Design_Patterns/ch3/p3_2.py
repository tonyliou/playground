# p3_2.py
class InteractiveObject:
    """進行交流的物件"""
    pass

class InteractiveObjectImplA:
    """實現類A"""
    pass

class InteractiveObjectImplB:
    """實現類B"""
    pass

class Meditor:
    """仲介類"""
    def __init__(self):
        self.__interactiveObjA = InteractiveObjectImplA()
        self.__interactiveObjB = InteractiveObjectImplB()
    def interative(self):
        """進行交流的操作"""
        # 通過self.__interactiveObjA和self.__interactiveObjB完成相應的交交互操作
        Pass
