#p1_4.py
import time
from abc import ABCMeta, abstractmethod
from p1_2 import Observer, Observable
# 導入時間處理模組
          
class Account(Observable):
    """用戶帳戶"""
    def __init__(self):
        super().__init__()
        self.__latestIp = {}
        self.__latestRegion = {}
    def login(self, name, ip, time):
        region = self.__getRegion(ip)
        if self.__isLongDistance(name, region):
            self.notifyObservers({"name": name, "ip": ip, "region": region, "time": time})
        self.__latestRegion[name] = region
        self.__latestIp[name] = ip
    def __getRegion(self, ip):
        # 由IP位址獲取地區資訊。這裡只是模擬，真實項目中應該調用IP位址解析服務
        ipRegions = {
            "101.47.18.9": "浙江省杭州市",
            "67.218.147.69":"美國洛杉磯"
        }
        region = ipRegions.get(ip)
        return "" if region is None else region
    def __isLongDistance(self, name, region):
        # 計算本次登錄與最近幾次登錄的地區差距
        # 這裡只是簡單地用字串匹配來類比，真實的專案中應該調用地理資訊相關的服務
        latestRegion = self.__latestRegion.get(name)
        return latestRegion is not None and latestRegion != region;

class SmsSender():
    """短信發送器"""
    def update(self, observable, object):
        print("[短信發送] " + object["name"] + "您好！檢測到您的帳戶可能登錄異常。最近一次登錄資訊：\n"
              + "登錄地區：" + object["region"] + "  登錄ip：" + object["ip"] + "  登錄時間："
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))

class MailSender():
    """郵件發送器"""
    def update(self, observable, object):
        print("[郵件發送] " + object["name"] + "您好！檢測到您的帳戶可能登錄異常。最近一次登錄資訊：\n"
              + "登錄地區：" + object["region"] + "  登錄ip：" + object["ip"] + "  登錄時間："
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))

def testLogin():
    accout = Account()
    accout.addObserver(SmsSender())
    accout.addObserver(MailSender())
    accout.login("Tony", "101.47.18.9", time.time())
    accout.login("Tony", "67.218.147.69", time.time())

testLogin()


