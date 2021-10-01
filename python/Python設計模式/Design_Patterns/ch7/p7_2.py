# p7_2.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class Request:
    """請求(內容)"""
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

class Responsible(metaclass=ABCMeta):
    """責任人抽象類別"""
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
    def getNextHandler(self):
        return self._nextHandler
    def handleRequest(self, request):
        """請求處理"""
        # 當前責任人處理請求
        self._handleRequestImpl(request)
        # 如果存在下一個責任人，則將請求傳遞(提交)給下一個責任人
        if (self._nextHandler is not None):
            self._nextHandler.handleRequest(request)
    @abstractmethod
    def _handleRequestImpl(self, request):
        """真正處理請求的方法"""
        pass
