# p6_2.py
from copy import copy, deepcopy

class PetStore:
    """寵物店"""
    def __init__(self, name):
        self.__name = name
        self.__petList = []
    def setName(self, name):
        self.__name = name
    def showMyself(self):
        print("%s 寵物店有以下寵物：" % self.__name)
        for pet in self.__petList:
            print(pet + "\t", end="")
        print()
    def addPet(self, pet):
        self.__petList.append(pet)

def testPetStore():
    petter = PetStore("Petter")
    petter.addPet("小狗Coco")
    print("父本petter：", end="")
    petter.showMyself()
    print()

    petter1 = deepcopy(petter)
    petter1.addPet("小貓Amy")
    print("副本petter1：", end="")
    petter1.showMyself()
    print("父本petter：", end="")
    petter.showMyself()
    print()

    petter2 = copy(petter)
    petter2.addPet("小兔Ricky")
    print("副本petter2：", end="")
    petter2.showMyself()
    print("父本petter：", end="")
    petter.showMyself()

testPetStore()

