# p5_1.py
class MyBeautifulGril(object):
    """我的漂亮女神"""
    __instance = None
    __isFirstInit = False
    def __new__(cls, name):
        if not cls.__instance:
            MyBeautifulGril.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            print("遇見" + name + "，我一見鍾情！")
            MyBeautifulGril.__isFirstInit = True
        else:
            print("遇見" + name + "，我置若罔聞！")
    def showMyHeart(self):
        print(self.__name + "就是我心中的唯一！")

def TestLove():
    jenny = MyBeautifulGril("Jenny")
    jenny.showMyHeart()
    kimi = MyBeautifulGril("Kimi")
    kimi.showMyHeart()
    print("id(jenny):", id(jenny), " id(kimi):", id(kimi))

TestLove()

