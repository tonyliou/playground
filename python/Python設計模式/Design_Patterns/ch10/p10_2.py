# p10_2.py
class BaseIterator:
    """反覆運算器"""
    def __init__(self, data):
        self.__data = data
        self.toBegin()
    def toBegin(self):
        """將指針移至起始位置"""
        self.__curIdx = -1
    def toEnd(self):
        """將指針移至結尾位置"""
        self.__curIdx = len(self.__data)
    def next(self):
        """移動至下一個元素"""
        if (self.__curIdx < len(self.__data) - 1):
            self.__curIdx += 1
            return True
        else:
            return False
    def previous(self):
        "移動至上一個元素"
        if (self.__curIdx > 0):
            self.__curIdx -= 1
            return True
        else:
            return False
    def current(self):
        """獲取當前的元素"""
        return self.__data[self.__curIdx] if (self.__curIdx < len(self.__data) and self.__curIdx >= 0) else None

def testBaseIterator():
    print("從前往後遍歷:")
    iterator = BaseIterator(range(0, 10))
    while(iterator.next()):
        customer = iterator.current()
        print(customer, end="\t")
    print()
    print("從後往前遍歷:")
    iterator.toEnd()
    while (iterator.previous()):
        customer = iterator.current()
        print(customer, end="\t")

testBaseIterator()
