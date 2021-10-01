# p6_1.py
from copy import copy, deepcopy

class Person:
    """人"""
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def showMyself(self):
        print("我是" + self.__name + "，年齡" + str(self.__age) + "。")
    def coding(self):
        print("我是碼農，我用程式改變世界，Coding……")
    def reading(self):
        print("閱讀使我快樂！知識使我成長！如饑似渴地閱讀是生活的一部分……")
    def fallInLove(self):
        print("春風吹，月亮明，花前月下好相約……")
    def clone(self):
        return copy(self)

def testClone():
    tony = Person("Tony", 27)
    tony.showMyself()
    tony.coding()
    tony1 = tony.clone()
    tony1.showMyself()
    tony1.reading()
    tony2 = tony.clone()
    tony2.showMyself()
    tony2.fallInLove()

testClone()


