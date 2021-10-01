# p2_1.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class Water:
    """水(H2O)"""
    def __init__(self, state):
        self.__temperature = 25 # 默認常溫為25℃
        self.__state = state
    def setState(self, state):
        self.__state = state
    def changeState(self, state):
        if (self.__state):
            print("由", self.__state.getName(), "變為", state.getName())
        else:
            print("初始化為", state.getName())
        self.__state = state
    def getTemperature(self):
        return self.__temperature
    def setTemperature(self, temperature):
        self.__temperature = temperature
        if (self.__temperature <= 0):
            self.changeState(SolidState("固態"))
        elif (self.__temperature <= 100):
            self.changeState(LiquidState("液態"))
        else:
            self.changeState(GaseousState("氣態"))
    def riseTemperature(self, step):
        self.setTemperature(self.__temperature + step)
    def reduceTemperature(self, step):
        self.setTemperature(self.__temperature - step)
    def behavior(self):
        self.__state.behavior(self)
        
class State(metaclass=ABCMeta):
    """狀態類別"""
    def __init__(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    @abstractmethod
    def behavior(self, water):
        """不同狀態下的行為"""
        pass

class SolidState(State):
    """固態"""
    def __init__(self, name):
        super().__init__(name)
    def behavior(self, water):
        print("我性格高冷，當前體溫" + str(water.getTemperature()) +
              "℃，我堅如鋼鐵，仿如一冷血動物，請用我砸人，嘿嘿……")

class LiquidState(State):
    """液態"""
    def __init__(self, name):
        super().__init__(name)
    def behavior(self, water):
        print("我性格溫和，當前體溫" + str(water.getTemperature()) +
              "℃，我可滋潤萬物，飲用我可讓你活力倍增……")

class GaseousState(State):
    """氣態"""
    def __init__(self, name):
        super().__init__(name)
    def behavior(self, water):
        print("我性格熱烈，當前體溫" + str(water.getTemperature()) +
              "℃，飛向天空是我畢生的夢想，在這你將看不到我的存在，我將達到無我的境界……")

def testState():
    water = Water(LiquidState("液態"))
    # water = Water()
    water.behavior()
    water.setTemperature(-4)
    water.behavior()
    water.riseTemperature(18)
    water.behavior()
    water.riseTemperature(110)
    water.behavior()
    
testState()

