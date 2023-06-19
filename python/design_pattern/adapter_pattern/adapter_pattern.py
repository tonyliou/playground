class IHightPerson:
    "接口類，提供空實現的方法，由子類去實現"

    def getName(self):
        "獲取姓名"
        pass

    def getHeight(self):
        "獲取身高"
        pass


class HighPerson(IHightPerson):
    "個高的人"

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getHeight(self):
        return 170

class ShortPerson:
    "個矮的人"

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getRealHeight(self):
        return 160

    def getShoesHeight(self):
        return 6

class DecoratePerson(ShortPerson, IHightPerson):
    "有高跟鞋搭配的人"

    def getHeight(self):
        return super().getRealHeight() + super().getShoesHeight()

def canPlayReceptionist(person):
    """
    是否可以成為(高級酒店)接待員
    :param person: IHightPerson的對象
    :return: 是否符合做接待員的條件
    """
    return person.getHeight() >= 165;


def testPerson():
    lira = HighPerson("Lira")
    print(lira.getName() + "身高" + str(lira.getHeight()) + "，完美如你，天生的美女！" )
    print("是否適合做接待員：", "符合" if canPlayReceptionist(lira) else "不符合")
    print()
    demi = DecoratePerson("Demi");
    print(demi.getName() + "身高" + str(demi.getHeight()) + "在高跟鞋的適配下，你身高不輸高圓圓，氣質不輸范冰冰！")
    print("是否適合做接待員：", "符合" if canPlayReceptionist(lira) else "不符合")

testPerson()