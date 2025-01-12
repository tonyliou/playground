# p8_1.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class ReceiveParcel(metaclass=ABCMeta):
    """接收包裹抽象類別"""
    def __init__(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    @abstractmethod
    def receive(self, parcelContent):
        pass

class TonyReception(ReceiveParcel):
    """Tony接收"""
    def __init__(self, name, phoneNum):
        super().__init__(name)
        self.__phoneNum = phoneNum
    def getPhoneNum(self):
        return self.__phoneNum
    def receive(self, parcelContent):
        print("貨物主人：%s，手機號：%s" % (self.getName(), self.getPhoneNum()) )
        print("接收到一個包裹，包裹內容：%s" % parcelContent)

class WendyReception(ReceiveParcel):
    """Wendy代收"""
    def __init__(self, name, receiver):
        super().__init__(name)
        self.__receiver = receiver
    def receive(self, parcelContent):
        print("我是%s的朋友，我來幫他代收快遞！" % (self.__receiver.getName() + "") )
        if(self.__receiver is not None):
            self.__receiver.receive(parcelContent)
        print("代收人：%s" % self.getName())

def testReceiveParcel():
    tony = TonyReception("Tony", "18512345678")
    print("Tony接收：")
    tony.receive("雪地靴")
    print()

    print("Wendy代收：")
    wendy = WendyReception("Wendy", tony)
    wendy.receive("雪地靴")

testReceiveParcel()

