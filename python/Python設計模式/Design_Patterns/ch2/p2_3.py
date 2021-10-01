# p2_3.py
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

class Water(Context):
    """水(H2O)"""

    def __init__(self):
        super().__init__()
        self.addState(SolidState("固態"))
        self.addState(LiquidState("液態"))
        self.addState(GaseousState("氣態"))
        self.setTemperature(25)
    def getTemperature(self):
        return self._getStateInfo()
    def setTemperature(self, temperature):
        self._setStateInfo(temperature)
    def riseTemperature(self, step):
        self.setTemperature(self.getTemperature() + step)
    def reduceTemperature(self, step):
        self.setTemperature(self.getTemperature() - step)
    def behavior(self):
        state = self.getState()
        if(isinstance(state, State)):
            state.behavior(self)

# 單例的裝飾器
def singleton(cls, *args, **kwargs):
    "構造一個單例的裝飾器"
    instance = {}
    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return __singleton

@singleton
class SolidState(State):
    """固態"""
    def __init__(self, name):
        super().__init__(name)
    def isMatch(self, stateInfo):
        return stateInfo < 0
    def behavior(self, context):
        print("我性格高冷，當前體溫", context._getStateInfo(),
              "℃，我堅如鋼鐵，仿如一冷血動物，請用我砸人，嘿嘿……")

@singleton
class LiquidState(State):
    """液態"""
    def __init__(self, name):
        super().__init__(name)
    def isMatch(self, stateInfo):
        return (stateInfo >= 0 and stateInfo < 100)
    def behavior(self, context):
        print("我性格溫和，當前體溫", context._getStateInfo(),
              "℃，我可滋潤萬物，飲用我可讓你活力倍增……")

@singleton
class GaseousState(State):
    """氣態"""
    def __init__(self, name):
        super().__init__(name)
    def isMatch(self, stateInfo):
        return stateInfo >= 100
    def behavior(self, context):
        print("我性格熱烈，當前體溫", context._getStateInfo(),
              "℃，飛向天空是我畢生的夢想，在這你將看不到我的存在，我將達到無我的境界……")

def testState():
    #water = Water(LiquidState("液態"))
    water = Water()
    water.behavior()
    water.setTemperature(-4)
    water.behavior()
    water.riseTemperature(18)
    water.behavior()
    water.riseTemperature(110)
    water.behavior()

testState()

