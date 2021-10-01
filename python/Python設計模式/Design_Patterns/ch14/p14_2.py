# p14_2.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法

class Person:
    """人類"""
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    def showMysef(self):
        print("%s 年齡：%d歲，體重：%0.2fkg，身高：%0.2fm" % (self.name, self.age, self.weight, self.height) )

class ICompare(metaclass=ABCMeta):
    """比較演算法"""
    @abstractmethod
    def comparable(self, person1, person2):
        "person1 > person2 返回值>0，person1 == person2 返回0， person1 < person2 返回值小於0"
        pass

class CompareByAge(ICompare):
    """通過年齡排序"""
    def comparable(self, person1, person2):
        return person1.age - person2.age

class CompareByHeight(ICompare):
    """通過身高排序"""
    def comparable(self, person1, person2):
        return person1.height - person2.height

class SortPerson:
    "Person的排序類"
    def __init__(self, compare):
        self.__compare = compare
    def sort(self, personList):
        """排序演算法
        這裡採用最簡單的冒泡排序"""
        n = len(personList)
        for i in range(0, n-1):
            for j in range(0, n-i-1):
                if(self.__compare.comparable(personList[j], personList[j+1]) > 0):
                    tmp = personList[j]
                    personList[j] = personList[j+1]
                    personList[j+1] = tmp
            j += 1
        i += 1

def testSortPerson():
    personList = [
        Person("Tony", 2, 54.5, 0.82),
        Person("Jack", 31, 74.5, 1.80),
        Person("Nick", 54, 44.5, 1.59),
        Person("Eric", 23, 62.0, 1.78),
        Person("Helen", 16, 45.7, 1.60)
    ]
    ageSorter = SortPerson(CompareByAge())
    ageSorter.sort(personList)
    print("根據年齡進行排序後的結果：")
    for person in personList:
        person.showMysef()
    print()

    heightSorter = SortPerson(CompareByHeight())
    heightSorter.sort(personList)
    print("根據身高進行排序後的結果：")
    for person in personList:
        person.showMysef()
    print()

testSortPerson()
