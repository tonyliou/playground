# p10_6.py
from collections import Iterable, Iterator

class NumberSequence:
    """生成一個間隔為step的數位系列"""
    def __init__(self, init, step, max = 100):
        self.__data = init
        self.__step = step
        self.__max = max
    def __iter__(self):
        return self
    def __next__(self):
        if(self.__data < self.__max):
            tmp = self.__data
            self.__data += self.__step
            return tmp
        else:
            raise StopIteration

def testNumberSequence():
    numSeq = NumberSequence(0, 5, 20)
    print(isinstance(numSeq, Iterable))
    print(isinstance(numSeq, Iterator))
    for n in numSeq:
        print(n, end="\t")

testNumberSequence()
