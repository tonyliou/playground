# p19_3.py
from p19_2 import DataNode, Visitor, ObjectStructure

class DesignPatternBook(DataNode):
    """《從生活的角度解讀設計模式》一書"""
    def getName(self):
        return "《從生活的角度解讀設計模式》"

class Engineer(Visitor):
    """工程師"""
    def visit(self, book):
        print("技術人讀%s一書後的感受：能抓住模式的核心思想，深入淺出，很有見地！" % book.getName())

class ProductManager(Visitor):
    """產品經理"""
    def visit(self, book):
        print("產品經理讀%s一書後的感受：配圖非常有趣，文章很有層次感！" % book.getName())

class OtherFriend(Visitor):
    """IT圈外的朋友"""
    def visit(self, book):
        print("IT圈外的朋友讀%s一書後的感受：技術的內容一臉蒙，但故事很精彩，像看小說或故事集！"
              % book.getName())

def testVisitBook():
    book = DesignPatternBook()
    objMgr = ObjectStructure()
    objMgr.add(book)
    objMgr.action(Engineer())
    objMgr.action(ProductManager())
    objMgr.action(OtherFriend())

testVisitBook()
