# p23_5.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class Skill(metaclass=ABCMeta):
    """技能的抽象類別"""
    @abstractmethod
    def performance(self):
        """技能表演"""
        pass

class NewEmployee:
    """公司新員工"""
    def __init__(self, name):
        self.__name = name
    def doPerformance(self, skill):
        print(self.__name + "的表演:", end="")
        skill.performance()

class Sing(Skill):
    """唱歌"""
    def performance(self):
        print("唱一首歌")

class Joke(Skill):
    """說段子"""
    def performance(self):
        print("說一個搞笑段子")

class Dling(Skill):
    """拉Ukulele"""
    def performance(self):
        print("彈一首Ukulele曲子")

class PerformMagicTricks(Skill):
    """表演魔術"""
    def performance(self):
        print("神秘魔術")

class Skateboarding(Skill):
    """玩滑板"""
    def performance(self):
        print("酷炫滑板")

def testStrategySkill():
    helen = NewEmployee("Helen")
    helen.doPerformance(Sing())
    frank = NewEmployee("Frank")
    frank.doPerformance(Dling())
    jacky = NewEmployee("Jacky")
    jacky.doPerformance(Joke())
    chork = NewEmployee("Chork")
    chork.doPerformance(PerformMagicTricks())
    Kerry = NewEmployee("Kerry")
    Kerry.doPerformance(Skateboarding())

testStrategySkill()
