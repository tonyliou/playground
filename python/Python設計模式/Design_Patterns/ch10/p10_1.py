# p10_1.py
class Customer:
    """客戶"""
    def __init__(self, name):
        self.__name = name
        self.__num = 0
        self.__clinics = None
    def getName(self):
        return self.__name
    def register(self, system):
        system.pushCustomer(self)
    def setNum(self, num):
        self.__num = num
    def getNum(self):
        return self.__num
    def setClinic(self, clinic):
        self.__clinics = clinic
    def getClinic(self):
        return self.__clinics

class NumeralIterator:
    """反覆運算器"""
    def __init__(self, data):
        self.__data = data
        self.__curIdx = -1
    def next(self):
        """移動至下一個元素"""
        if (self.__curIdx < len(self.__data) - 1):
            self.__curIdx += 1
            return True
        else:
            return False
    def current(self):
        """獲取當前的元素"""
        return self.__data[self.__curIdx] if (self.__curIdx < len(self.__data) and self.__curIdx >= 0) else None

class NumeralSystem:
    """排號系統"""
    __clinics = ("1號診室", "2號診室", "3號診室")
    def __init__(self, name):
        self.__customers = []
        self.__curNum = 0
        self.__name = name
    def pushCustomer(self, customer):
        customer.setNum(self.__curNum + 1)
        click = NumeralSystem.__clinics[self.__curNum % len(NumeralSystem.__clinics)]
        customer.setClinic(click)
        self.__curNum += 1
        self.__customers.append(customer)
        print("%s 您好！您已在%s成功掛號，序號：%04d，請耐心等待！"
              % (customer.getName(), self.__name, customer.getNum()) )
    def getIterator(self):
        return NumeralIterator(self.__customers)

def testHospital():
    numeralSystem = NumeralSystem("掛號台")
    lily = Customer("Lily")
    lily.register(numeralSystem);
    pony = Customer("Pony")
    pony.register(numeralSystem)
    nick = Customer("Nick")
    nick.register(numeralSystem)
    tony = Customer("Tony")
    tony.register(numeralSystem)
    print()
    iterator = numeralSystem.getIterator()
    while(iterator.next()):
        customer = iterator.current()
        print("下一位病人 %04d(%s) 請到 %s 就診。"
              % (customer.getNum(), customer.getName(), customer.getClinic()) )

testHospital()
