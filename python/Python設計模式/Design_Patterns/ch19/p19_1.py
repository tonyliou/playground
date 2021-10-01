# p19_1.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class DesignPatternBook:
    """《從生活的角度解讀設計模式》一書"""
    def getName(self):
        return "《從生活的角度解讀設計模式》"

class Reader(metaclass=ABCMeta):
    """訪問者，也就是讀者"""
    @abstractmethod
    def read(self, book):
        pass

class Engineer(Reader):
    """工程師"""
    def read(self, book):
        print("技術人讀%s一書後的感受：能抓住模式的核心思想，深入淺出，很有見地！" % book.getName())

class ProductManager(Reader):
    """產品經理"""
    def read(self, book):
        print("產品經理讀%s一書後的感受：配圖非常有趣，文章很有層次感！" % book.getName())

class OtherFriend(Reader):
    """IT圈外的朋友"""
    def read(self, book):
        print("IT圈外的朋友讀%s一書後的感受：技術的內容一臉懵，但故事很精彩，像看小說或故事集！"
              % book.getName())

def testBook():
    book = DesignPatternBook()
    fans = [Engineer(), ProductManager(), OtherFriend()];
    for fan in fans:
        fan.read(book)

testBook()
