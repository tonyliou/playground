# p8_3.py
from p8_2 import Subject, ProxySubject

class TonyReception(Subject):
    """Tony接收"""
    def __init__(self, name, phoneNum):
        super().__init__(name)
        self.__phoneNum = phoneNum
    def getPhoneNum(self):
        return self.__phoneNum
    def request(self, content):
        print("貨物主人：%s，手機號：%s" % (self.getName(), self.getPhoneNum()))
        print("接收到一個包裹，包裹內容：%s" % str(content))

class WendyReception(ProxySubject):
    """Wendy代收"""
    def __init__(self, name, receiver):
        super().__init__(name, receiver)
    def preRequest(self):
        print("我是%s的朋友，我來幫他代收快遞！" % (self._realSubject.getName() + ""))
    def afterRequest(self):
        print("代收人：%s" % self.getName())

def testReceiveParcel2():
    tony = TonyReception("Tony", "18512345678")
    print("Tony接收：")
    tony.request("雪地靴")
    print()
    print("Wendy代收：")
    wendy = WendyReception("Wendy", tony)
    wendy.request("雪地靴")

testReceiveParcel2()
