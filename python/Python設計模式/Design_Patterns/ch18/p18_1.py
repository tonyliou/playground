# p18_1.py
import logging
# 引入logging模組記錄異常

class Pigment:
    """顏料"""
    def __init__(self, color):
        self.__color = color
        self.__user = ""
    def getColor(self):
        return self.__color
    def setUser(self, user):
        self.__user = user
        return self
    def showInfo(self):
        print("%s 取得 %s色顏料"  % (self.__user, self.__color) )

class PigmengFactory:
    """顏料的工廠類別"""
    def __init__(self):
        self.__sigmentSet = {
            "紅": Pigment("紅"),
            "黃": Pigment("黃"),
            "藍": Pigment("藍"),
            "綠": Pigment("綠"),
            "紫": Pigment("紫"),
        }
    def getPigment(self, color):
        pigment = self.__sigmentSet.get(color)
        if pigment is None:
            logging.error("沒有%s顏色的顏料！", color)
        return pigment

def testPigment():
    factory = PigmengFactory()
    pigmentRed = factory.getPigment("紅").setUser("夢之隊")
    pigmentRed.showInfo()
    pigmentYellow = factory.getPigment("黃").setUser("夢之隊")
    pigmentYellow.showInfo()
    pigmentBlue1 = factory.getPigment("藍").setUser("夢之隊")
    pigmentBlue1.showInfo()
    pigmentBlue2 = factory.getPigment("藍").setUser("和平隊")
    pigmentBlue2.showInfo()

testPigment()
