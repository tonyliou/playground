# p23_3.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class Strategy(metaclass=ABCMeta):
    """演算法的抽象類別"""
    @abstractmethod
    def algorithm(self, *args, **kwargs):
        """定義演算法"""
        Pass

class StrategyA(Strategy):
    """策略A"""
    def algorithm(self, *args, **kwargs):
        print("演算法A的實現...")

class StrategyB(Strategy):
    """策略B"""
    def algorithm(self, *args, **kwargs):
        print("演算法B的實現...")

class Context:
    """上下文環境類"""
    def interface(self, strategy, *args, **kwargs):
        """交互介面"""
        print("回檔執行前的操作")
        strategy.algorithm()
        print("回檔執行後的操作")

# 調用方式
context = Context()
context.interface(StrategyA())
context.interface(StrategyB())
