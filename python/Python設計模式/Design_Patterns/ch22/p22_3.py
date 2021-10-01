# p22_3.py
from p22_2 import ObjectPool, PooledObject

class PowerBank:
    """移動電源"""
    def __init__(self, serialNum, electricQuantity):
        self.__serialNum = serialNum
        self.__electricQuantity = electricQuantity
        self.__user = ""
    def getSerialNum(self):
        return self.__serialNum
    def getElectricQuantity(self):
        return self.__electricQuantity
    def setUser(self, user):
        self.__user = user
    def getUser(self):
        return self.__user
    def showInfo(self):
        print("序號:%03d  電量:%d%%  使用者:%s" % (self.__serialNum, self.__electricQuantity, self.__user))

class PowerBankPool(ObjectPool):
    """存放移動電源的智慧箱盒"""
    __serialNum = 0
    @classmethod
    def getSerialNum(cls):
        cls.__serialNum += 1
        return cls.__serialNum
    def createPooledObject(self):
        powerBank = PowerBank(PowerBankPool.getSerialNum(), 100)
        return PooledObject(powerBank)

def testObjectPool():
    powerBankPool = PowerBankPool()
    powerBank1 = powerBankPool.borrowObject()
    if (powerBank1 is not None):
        powerBank1.setUser("Tony")
        powerBank1.showInfo()
    powerBank2 = powerBankPool.borrowObject()
    if (powerBank2 is not None):
        powerBank2.setUser("Sam")
        powerBank2.showInfo()
    powerBankPool.returnObject(powerBank1)
    # powerBank1歸還後，不能再對其進行相關操作
    powerBank3 = powerBankPool.borrowObject()
    if (powerBank3 is not None):
        powerBank3.setUser("Aimee")
        powerBank3.showInfo()
    powerBankPool.returnObject(powerBank2)
    powerBankPool.returnObject(powerBank3)
    powerBankPool.clear()

testObjectPool()
