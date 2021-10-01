# p8_2.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class Subject(metaclass=ABCMeta):
    """主題類"""
    def __init__(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    @abstractmethod
    def request(self, content = ''):
        pass

class RealSubject(Subject):
    """真實主題類"""
    def request(self, content):
        print("RealSubject todo something...")

class ProxySubject(Subject):
    """代理主題類"""
    def __init__(self, name, subject):
        super().__init__(name)
        self._realSubject = subject
    def request(self, content = ''):
        self.preRequest()
        if(self._realSubject is not None):
            self._realSubject.request(content)
        self.afterRequest()
    def preRequest(self):
        print("preRequest")
    def afterRequest(self):
        print("afterRequest")

def testProxy():
    realObj = RealSubject('RealSubject')
    proxyObj = ProxySubject('ProxySubject', realObj)
    proxyObj.request()

testProxy()
