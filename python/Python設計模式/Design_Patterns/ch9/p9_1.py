# p9_1.py
class Register:
    """報到登記"""
    def register(self, name):
        print("活動中心:%s同學報到成功！" % name)

class Payment:
    """繳費中心"""
    def pay(self, name, money):
        print("繳費中心:收到%s同學%s元付款，繳費成功！" % (name, money) )

class DormitoryManagementCenter:
    """生活中心(宿舍管理中心)"""
    def provideLivingGoods(self, name):
        print("生活中心:%s同學的生活用品已發放。" % name)

class Dormitory:
    """宿舍"""
    def meetRoommate(self, name):
        print("宿    舍:" + "大家好！這是剛來的%s同學，是你們未來需要共度四年的室友！相互認識一下……" % name)

class Volunteer:
    """迎新志願者"""
    def __init__(self, name):
        self.__name = name
        self.__register = Register()
        self.__payment = Payment()
        self.__lifeCenter = DormitoryManagementCenter()
        self.__dormintory = Dormitory()
    def welcomeFreshmen(self, name):
        print("你好,%s同學! 我是新生報到的志願者%s，我將帶你完成整個報到流程。" % (name, self.__name))
        self.__register.register(name)
        self.__payment.pay(name, 10000)
        self.__lifeCenter.provideLivingGoods(name)
        self.__dormintory.meetRoommate(name)

def testRegister():
    volunteer = Volunteer("Frank")
    volunteer.welcomeFreshmen("Tony")

testRegister()
