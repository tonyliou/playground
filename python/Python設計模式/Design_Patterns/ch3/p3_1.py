# p3_1.py
class HouseInfo:
    """房源信息"""
    def __init__(self, area, price, hasWindow, hasBathroom, hasKitchen, address, owner):
        self.__area = area
        self.__price = price
        self.__hasWindow = hasWindow
        self.__hasBathroom = hasBathroom
        self.__hasKitchen = hasKitchen
        self.__address = address
        self.__owner = owner
    def getAddress(self):
        return self.__address
    def getOwnerName(self):
        return self.__owner.getName()
    def showInfo(self, isShowOwner = True):
        print("面積:" + str(self.__area) + "平方米",
              "價格:" + str(self.__price) + "元",
              "窗戶:" + ("有" if self.__hasWindow else "沒有"),
              "衛生間:" + self.__hasBathroom,
              "廚房:" + ("有" if self.__hasKitchen else "沒有"),
              "地址:" + self.__address,
              "房東:" + self.getOwnerName() if isShowOwner else "")

class HousingAgency:
    """房屋仲介"""
    def __init__(self, name):
        self.__houseInfos = []
        self.__name = name
    def getName(self):
        return self.__name
    def addHouseInfo(self, houseInfo):
        self.__houseInfos.append(houseInfo)
    def removeHouseInfo(self, houseInfo):
        for info in self.__houseInfos:
            if(info == houseInfo):
                self.__houseInfos.remove(info)
    def getSearchCondition(self, description):
        """這裡有一個將使用者描述資訊轉換成搜索條件的邏輯
        (為節省篇幅這裡原樣返回描述)"""
        return description
    def getMatchInfos(self, searchCondition):
        """根據房源資訊的各個屬性查找最匹配的資訊
        (為節省篇幅這裡略去匹配的過程，全部輸出)"""
        print(self.getName(), "為您找到以下最適合的房源：")
        for info in self.__houseInfos:
            info.showInfo(False)
        return  self.__houseInfos
    def signContract(self, houseInfo, period):
        """與房東簽訂協定"""
        print(self.getName(), "與房東", houseInfo.getOwnerName(), "簽訂", houseInfo.getAddress(),
              "的房子的租賃合同，租期", period, "年。 合同期內", self.getName(), "有權對其進行使用和轉租！")
    def signContracts(self, period):
        for info in self.__houseInfos :
            self.signContract(info, period)

class HouseOwner:
    """房東"""
    def __init__(self, name):
        self.__name = name
        self.__houseInfo = None
    def getName(self):
        return self.__name
    def setHouseInfo(self, address, area, price, hasWindow, bathroom, kitchen):
        self.__houseInfo = HouseInfo(area, price, hasWindow, bathroom, kitchen, address, self)
    def publishHouseInfo(self, agency):
        agency.addHouseInfo(self.__houseInfo)
        print(self.getName() + "在", agency.getName(), "發佈房源出租資訊：")
        self.__houseInfo.showInfo()

class Customer:
    """用戶，租房的貧下中農"""
    def __init__(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def findHouse(self, description, agency):
        print("我是" + self.getName() + ", 我想要找一個\"" + description + "\"的房子")
        print()
        return agency.getMatchInfos(agency.getSearchCondition(description))
    def seeHouse(self, houseInfos):
        """去看房，選擇最實用的房子
        (這裡省略看房的過程)"""
        size = len(houseInfos)
        return houseInfos[size-1]
    def signContract(self, houseInfo, agency, period):
        """與仲介簽訂協定"""
        print(self.getName(), "與仲介", agency.getName(), "簽訂", houseInfo.getAddress(),
              "的房子的租賃合同, 租期", period, "年。合同期內", self.__name, "有權對其進行使用！")

def testRenting():
    myHome = HousingAgency("我爱我家")
    zhangsan = HouseOwner("张三");
    zhangsan.setHouseInfo("上地西里", 20, 2500, 1, "独立卫生间", 0)
    zhangsan.publishHouseInfo(myHome)
    lisi = HouseOwner("李四")
    lisi.setHouseInfo("当代城市家园", 16, 1800, 1, "公用卫生间", 0)
    lisi.publishHouseInfo(myHome)
    wangwu = HouseOwner("王五")
    wangwu.setHouseInfo("金隅美和园", 18, 2600, 1, "独立卫生间", 1)
    wangwu.publishHouseInfo(myHome)
    print()

    myHome.signContracts(3)
    print()

    tony = Customer("Tony")
    houseInfos = tony.findHouse("18平米左右，要有独卫，要有窗户，最好是朝南，有厨房更好！价位在2000左右", myHome)
    print()
    print("正在看房，寻找最合适的住巢……")
    print()
    AppropriateHouse = tony.seeHouse(houseInfos)
    tony.signContract(AppropriateHouse, myHome, 1)

testRenting()


