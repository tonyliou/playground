# p19_4.py
from p19_2 import DataNode, Visitor, ObjectStructure

class Animal(DataNode):
    """動物類別"""
    def __init__(self, name, isMale, age, weight):
        self.__name = name
        self.__isMale = isMale
        self.__age = age
        self.__weight = weight
    def getName(self):
        return self.__name
    def isMale(self):
        return self.__isMale
    def getAge(self):
        return self.__age
    def getWeight(self):
        return self.__weight

class Cat(Animal):
    """貓"""
    def __init__(self, name, isMale, age, weight):
        super().__init__(name, isMale, age, weight)
    def speak(self):
        print("miao~")

class Dog(Animal):
    """狗"""
    def __init__(self,  name, isMale, age, weight):
        super().__init__( name, isMale, age, weight)
    def speak(self):
        print("wang~")

class GenderCounter(Visitor):
    """性別統計"""
    def __init__(self):
        self.__maleCat = 0
        self.__femaleCat = 0
        self.__maleDog = 0
        self.__femalDog = 0
    def visit(self, data):
        if isinstance(data, Cat):
            if data.isMale():
                self.__maleCat += 1
            else:
                self.__femaleCat += 1
        elif isinstance(data, Dog):
            if data.isMale():
                self.__maleDog += 1
            else:
                self.__femalDog += 1
        else:
            print("Not support this type")
    def getInfo(self):
        print("%d只雄貓，%d只雌貓，%d只雄狗，%d只雌狗。"
              % (self.__maleCat, self.__femaleCat, self.__maleDog, self.__femalDog) )

class WeightCounter(Visitor):
    """體重的統計"""
    def __init__(self):
        self.__catNum = 0
        self.__catWeight = 0
        self.__dogNum = 0
        self.__dogWeight  = 0
    def visit(self, data):
        if isinstance(data, Cat):
            self.__catNum +=1
            self.__catWeight += data.getWeight()
        elif isinstance(data, Dog):
            self.__dogNum += 1
            self.__dogWeight += data.getWeight()
        else:
            print("Not support this type")
    def getInfo(self):
        print("貓的平均體重是：%0.2fkg， 狗的平均體重是：%0.2fkg" %
              ((self.__catWeight / self.__catNum),(self.__dogWeight / self.__dogNum)))

class AgeCounter(Visitor):
    """年齡統計"""
    def __init__(self):
        self.__catMaxAge = 0
        self.__dogMaxAge = 0
    def visit(self, data):
        if isinstance(data, Cat):
            if self.__catMaxAge < data.getAge():
                self.__catMaxAge = data.getAge()
        elif isinstance(data, Dog):
            if self.__dogMaxAge < data.getAge():
                self.__dogMaxAge = data.getAge()
        else:
            print("Not support this type")
    def getInfo(self):
        print("貓的最大年齡是：%s，狗的最大年齡是：%s" % (self.__catMaxAge, self.__dogMaxAge) )

def testAnimal():
    animals = ObjectStructure()
    animals.add(Cat("Cat1", True, 1, 5))
    animals.add(Cat("Cat2", False, 0.5, 3))
    animals.add(Cat("Cat3", False, 1.2, 4.2))
    animals.add(Dog("Dog1", True, 0.5, 8))
    animals.add(Dog("Dog2", True, 3, 52))
    animals.add(Dog("Dog3", False, 1, 21))
    animals.add(Dog("Dog4", False, 2, 25))
    genderCounter = GenderCounter()
    animals.action(genderCounter)
    genderCounter.getInfo()
    print()

    weightCounter = WeightCounter()
    animals.action(weightCounter)
    weightCounter.getInfo()
    print()

    ageCounter = AgeCounter()
    animals.action(ageCounter)
    ageCounter.getInfo()

testAnimal()
