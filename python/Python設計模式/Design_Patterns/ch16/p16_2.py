# p16_2.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class Command(metaclass=ABCMeta):
    """命令的抽象類別"""
    @abstractmethod
    def execute(self):
        pass

class CommandImpl(Command):
    """命令的具體實現類別"""
    def __init__(self, receiver):
        self.__receiver = receiver
    def execute(self):
        self.__receiver.doSomething()

class Receiver:
    """命令的接收者"""
    def doSomething(self):
        print("do something...")

class Invoker:
    """調度者"""
    def __init__(self):
        self.__command = None
    def setCommand(self, command):
        self.__command = command
    def action(self):
        if self.__command is not None:
            self.__command.execute()
