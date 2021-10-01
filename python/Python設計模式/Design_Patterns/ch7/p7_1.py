#p7_1.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class Person:
    """請假申請人"""
    def __init__(self, name, dayoff, reason):
        self.__name = name
        self.__dayoff = dayoff
        self.__reason = reason
        self.__leader = None
    def getName(self):
        return self.__name
    def getDayOff(self):
        return self.__dayoff
    def getReason(self):
        return self.__reason
    def setLeader(self, leader):
        self.__leader = leader
    def reuqest(self):
        print("%s 申請請假 %d 天。請假事由：%s" % (self.__name, self.__dayoff, self.__reason) )
        if( self.__leader is not None):
            self.__leader.handleRequest(self)

class Manager(metaclass=ABCMeta):
    """公司管理人員"""
    def __init__(self, name, title):
        self.__name = name
        self.__title = title
        self._nextHandler = None
    def getName(self):
        return self.__name
    def getTitle(self):
        return self.__title
    def setNextHandler(self, nextHandler):
        self._nextHandler = nextHandler
    @abstractmethod
    def handleRequest(self, person):
        pass

class Supervisor(Manager):
    """主管"""
    def __init__(self, name, title):
        super().__init__(name, title)
    def handleRequest(self, person):
        if(person.getDayOff() <= 2):
            print("同意 %s 請假，簽字人：%s(%s)" % (person.getName(), self.getName(), self.getTitle()) )
        if(self._nextHandler is not None):
            self._nextHandler.handleRequest(person)

class DepartmentManager(Manager):
    """部門總監"""
    def __init__(self, name, title):
        super().__init__(name, title)
    def handleRequest(self, person):
        if(person.getDayOff() >2 and person.getDayOff() <= 5):
            print("同意 %s 請假，簽字人：%s(%s)" % (person.getName(), self.getName(), self.getTitle()))
        if(self._nextHandler is not None):
            self._nextHandler.handleRequest(person)

class CEO(Manager):
    """CEO"""
    def __init__(self, name, title):
        super().__init__(name, title)
    def handleRequest(self, person):
        if (person.getDayOff() > 5 and person.getDayOff() <= 22):
            print("同意 %s 請假，簽字人：%s(%s)" % (person.getName(), self.getName(), self.getTitle()))
        if (self._nextHandler is not None):
            self._nextHandler.handleRequest(person)

class Administrator(Manager):
    """行政人員"""
    def __init__(self, name, title):
        super().__init__(name, title)
    def handleRequest(self, person):
        print("%s 的請假申請已審核，情況屬實！已備案處理。處理人：%s(%s)\n" % (person.getName(), self.getName(), self.getTitle()))

def testAskForLeave():
    directLeader = Supervisor("Eren", "用戶端研發部經理")
    departmentLeader = DepartmentManager("Eric", "技術研發中心總監")
    ceo = CEO("Helen", "創新文化公司CEO")
    administrator = Administrator("Nina", "行政中心總監")
    directLeader.setNextHandler(departmentLeader)
    departmentLeader.setNextHandler(ceo)
    ceo.setNextHandler(administrator)

    sunny = Person("Sunny", 1, "參加MDCC大會。")
    sunny.setLeader(directLeader)
    sunny.reuqest()
    tony = Person("Tony", 5, "家裡有緊急事情！")
    tony.setLeader(directLeader)
    tony.reuqest()
    pony = Person("Pony", 15, "出國深造。")
    pony.setLeader(directLeader)
    pony.reuqest()

testAskForLeave()




