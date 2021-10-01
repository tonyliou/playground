# p2_2.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class Context(metaclass=ABCMeta):
    """狀態模式的上下文環境類別"""
    def __init__(self):
        self.__states = []
        self.__curState = None
        # 狀態發生變化依賴的屬性, 當這一變數由多個變數共同決定時可以將其單獨定義成一個類
        self.__stateInfo = 0
    def addState(self, state):
        if (state not in self.__states):
            self.__states.append(state)
    def changeState(self, state):
        if (state is None):
            return False
        if (self.__curState is None):
            print("初始化為", state.getName())
        else:
            print("由", self.__curState.getName(), "變為", state.getName())
        self.__curState = state
        self.addState(state)
        return True
    def getState(self):
        return self.__curState
    def _setStateInfo(self, stateInfo):
        self.__stateInfo = stateInfo
        for state in self.__states:
            if( state.isMatch(stateInfo) ):
                self.changeState(state)
    def _getStateInfo(self):
        return self.__stateInfo

class State:
    """狀態的基類別"""
    def __init__(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def isMatch(self, stateInfo):
        "狀態的屬性stateInfo是否在當前的狀態範圍內"
        return False
    @abstractmethod
    def behavior(self, context):
        pass
