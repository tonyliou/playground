# p20_2.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class ReaderView(metaclass=ABCMeta):
    """閱讀器視圖"""
    def __init__(self):
        self.__curPageNum = 1
    def getPage(self, pageNum):
        self.__curPageNum = pageNum
        return "第" + str(pageNum) + "頁的內容"
    def prePage(self):
        """範本方法，往前翻一頁"""
        content = self.getPage(self.__curPageNum - 1)
        self._displayPage(content)
    def nextPage(self):
        """範本方法，往後翻一頁"""
        content = self.getPage(self.__curPageNum + 1)
        self._displayPage(content)
    @abstractmethod
    def _displayPage(self, content):
        """翻頁效果"""
        pass

class SmoothView(ReaderView):
    """左右平滑的視圖"""
    def _displayPage(self, content):
        print("左右平滑:" + content)

class SimulationView(ReaderView):
    """模擬翻頁的視圖"""
    def _displayPage(self, content):
        print("模擬翻頁:" + content)

def testReader():
    smoothView = SmoothView()
    smoothView.nextPage()
    smoothView.prePage()

    simulationView = SimulationView()
    simulationView.nextPage()
    simulationView.prePage()

testReader()
