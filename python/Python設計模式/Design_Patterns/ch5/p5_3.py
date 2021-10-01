# p5_3.py
class Singleton2(type):
    """單例實現方式二"""
    def __init__(cls, what, bases=None, dict=None):
        super().__init__(what, bases, dict)
        cls._instance = None # 初始化全域變數cls._instance為None
    def __call__(cls, *args, **kwargs):
        # 控制物件的創建過程，如果cls._instance為None，則創建，否則直接返回
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class CustomClass(metaclass=Singleton2):
    """用戶自訂的類"""
    def __init__(self, name):
        self.__name = name
    def getName(self):
        return self.__name

tony = CustomClass("Tony")
karry = CustomClass("Karry")
print(tony.getName(), karry.getName())
print("id(tony):", id(tony), "id(karry):", id(karry))
print("tony == karry:", tony == karry)
