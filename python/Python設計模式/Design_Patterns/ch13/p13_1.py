# p13_1.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class SocketEntity:
    """介面類別型定義"""
    def __init__(self, numOfPin, typeOfPin):
        self.__numOfPin = numOfPin
        self.__typeOfPin = typeOfPin
    def getNumOfPin(self):
        return self.__numOfPin
    def setNumOfPin(self, numOfPin):
        self.__numOfPin = numOfPin
    def getTypeOfPin(self):
        return self.__typeOfPin
    def setTypeOfPin(self, typeOfPin):
        self.__typeOfPin = typeOfPin

class ISocket(metaclass=ABCMeta):
    """插座類別型"""
    def getName(self):
        """插座名稱"""
        pass
    def getSocket(self):
        """獲取介面"""
        pass

class ChineseSocket(ISocket):
    """國標插座"""
    def getName(self):
        return  "國標插座"
    def getSocket(self):
        return SocketEntity(3, "八字扁型")

class BritishSocket:
    """英標插座"""
    def name(self):
        return  "英標插座"
    def socketInterface(self):
        return SocketEntity(3, "T字方型")

class AdapterSocket(ISocket):
    """插座轉換器"""
    def __init__(self, britishSocket):
        self.__britishSocket = britishSocket
    def getName(self):
        return  self.__britishSocket.name() + "轉換器"
    def getSocket(self):
        socket = self.__britishSocket.socketInterface()
        socket.setTypeOfPin("八字扁型")
        return socket

def canChargeforDigtalDevice(name, socket):
    if socket.getNumOfPin() == 3 and socket.getTypeOfPin() == "八字扁型":
        isStandard = "符合"
        canCharge = "可以"
    else:
        isStandard = "不符合"
        canCharge = "不能"
    print("[%s]：\n針腳數量：%d，針腳類型：%s；%s中國標準，%s給中國內地的電子設備充電！"
          % (name, socket.getNumOfPin(), socket.getTypeOfPin(), isStandard, canCharge))
def testSocket():
    chineseSocket = ChineseSocket()
    canChargeforDigtalDevice(chineseSocket.getName(), chineseSocket.getSocket())
    britishSocket = BritishSocket()
    canChargeforDigtalDevice(britishSocket.name(), britishSocket.socketInterface())
    adapterSocket = AdapterSocket(britishSocket)

    canChargeforDigtalDevice(adapterSocket.getName(), adapterSocket.getSocket())

testSocket()
