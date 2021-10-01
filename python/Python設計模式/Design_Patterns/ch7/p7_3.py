# p7_3.py
from p7_2 import Responsible, Request
class Person:
    """請求者(請假人)"""
    def __init__(self, name):
        self.__name = name
        self.__leader = None
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setLeader(self, leader):
        self.__leader = leader
    def getLeader(self):
        return self.__leader
    def sendReuqest(self, request):
        print("%s 申請請假 %d 天。請假事由：%s" % (self.__name, request.getDayOff(), request.getReason()))
        if (self.__leader is not None):
            self.__leader.handleRequest(request)

class Supervisor(Responsible):
    """主管"""
    def __init__(self, name, title):
        super().__init__(name, title)
    def _handleRequestImpl(self, request):
        if (request.getDayOff() <= 2):
            print("同意 %s 請假，簽字人：%s(%s)" % (request.getName(), self.getName(), self.getTitle()))

class DepartmentManager(Responsible):
    """部門總監"""
    def __init__(self, name, title):
        super().__init__(name, title)
    def _handleRequestImpl(self, request):
        if (request.getDayOff() > 2 and request.getDayOff() <= 5):
            print("同意 %s 請假，簽字人：%s(%s)" % (request.getName(), self.getName(), self.getTitle()))

class CEO(Responsible):
    """CEO"""
    def __init__(self, name, title):
        super().__init__(name, title)
    def _handleRequestImpl(self, request):
        if (request.getDayOff() > 5 and request.getDayOff() <= 22):
            print("同意 %s 請假，簽字人：%s(%s)" % (request.getName(), self.getName(), self.getTitle()))

class Administrator(Responsible):
    """行政人員"""
    def __init__(self, name, title):
        super().__init__(name, title)
    def _handleRequestImpl(self, request):
        print("%s 的請假申請已審核，情況屬實！已備案處理。處理人：%s(%s)\n" % (request.getName(), self.getName(), self.getTitle()))

def testChainOfResponsibility():
    directLeader = Supervisor("Eren", "用戶端研發部經理")
    departmentLeader = DepartmentManager("Eric", "技術研發中心總監")
    ceo = CEO("Helen", "創新文化公司CEO")
    administrator = Administrator("Nina", "行政中心總監")
    directLeader.setNextHandler(departmentLeader)
    departmentLeader.setNextHandler(ceo)
    ceo.setNextHandler(administrator)

    sunny = Person("Sunny")
    sunny.setLeader(directLeader)
    sunny.sendReuqest(Request(sunny.getName(), 1, "參加MDCC大會。"))
    tony = Person("Tony")
    tony.setLeader(directLeader)
    tony.sendReuqest(Request(tony.getName(), 5, "家裡有緊急事情！"))
    pony = Person("Pony")
    pony.setLeader(directLeader)
    pony.sendReuqest(Request(pony.getName(), 15, "出國深造。"))

testChainOfResponsibility()





