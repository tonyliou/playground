# p26_7.py
from p26_6 import BirdAnimal, TerrestrialAnimal, AquaticAnimal 

class Monkey(TerrestrialAnimal):
    """猴子"""
    def __init__(self, name):
        super().__init__(name)

    def climbing(self):
        print(self._name + "在爬樹，動作靈活輕盈...")

# 修改Zoo類，增加climbing方法
class Zoo:
    """動物園"""
    def __init__(self):
        self.__animals =[]
    def addAnimal(self, animal):
        self.__animals.append(animal)
    def displayActivity(self):
        print("觀察每一種動物的活動方式：")
        for animal in self.__animals:
            animal.moving()
    def monkeyClimbing(self, monkey):
        monkey.climbing()

def testZoo():
    zoo = Zoo()
    zoo.addAnimal(TerrestrialAnimal("狗"))
    zoo.addAnimal(AquaticAnimal("魚"))
    zoo.addAnimal(BirdAnimal("鳥"))
    monkey = Monkey("猴子")
    zoo.addAnimal(monkey)
    zoo.displayActivity()
    print()
    print("觀察猴子的爬樹行為：")
    zoo.monkeyClimbing(monkey)

testZoo()
