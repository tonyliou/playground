# p0_7.py
class Person:
    "人"
    visited = 0
    def __init__(self, name, age, height):
        self.__name = name      	# 私有成員，存取權限為private
        self._age = age         	# 保護成員，存取權限為protected
        self.height = height    	# 公有成員，存取權限為public
    def getName(self):
        return self.__name
    def getAge(self):
        return self._age
    def showInfo(self):
        print("name:", self.__name)
        print("age:", self._age)
        print("height:", self.height)
        print("visited:", self.visited)
        Person.visited = Person.visited +1

class Teacher(Person):
    "老師"
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        self.__title = None
    def getTitle(self):
        return self.__title
    def setTitle(self, title):
        self.__title = title
    def showInfo(self):
        print("title:", self.__title)
        super().showInfo()

def testPerson():
    "測試方法"
    tony = Person("Tony", 25, 1.77)
    tony.showInfo()
    print();
    jenny = Teacher("Jenny", 34, 1.68);
    jenny.setTitle("教授");
    jenny.showInfo();

testPerson()
