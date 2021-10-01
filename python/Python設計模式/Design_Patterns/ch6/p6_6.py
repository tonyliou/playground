# p6_6.py
from p6_4 import Clone

class AppConfig(Clone):
    """應用程式功能配置"""
    def __init__(self, configName):
        self.__configName = configName
        self.parseFromFile("./config/default.xml")
    def parseFromFile(self, filePath):
        """
        從設定檔中解析配置項
        真實專案中通常會將配置保存到設定檔中，保證下次開啟時依然能夠生效；
        這裡為簡單起見，不從檔中讀取，以初始化的方式來類比。
        """
        self.__fontType = "宋體"
        self.__fontSize = 14
        self.__language = "中文"
        self.__logPath = "./logs/appException.log"
    def saveToFile(self, filePath):
        """
        將配置保存到設定檔中
        這裡為簡單起見，不再實現
        """
        pass
    def copyConfig(self, configName):
        """創建一個配置的副本"""
        config = self.deepClone()
        config.__configName = configName
        return config
    def showInfo(self):
        print("%s 的配置資訊如下：" % self.__configName)
        print("字體：", self.__fontType)
        print("字型大小：", self.__fontSize)
        print("語言：", self.__language)
        print("異常檔的路徑：", self.__logPath)
    def setFontType(self, fontType):
        self.__fontType = fontType
    def setFontSize(self, fontSize):
        self.__fontSize = fontSize
    def setLanguage(self, language):
        self.__language = language
    def setLogPath(self, logPath):
        self.__logPath = logPath

def testAppConfig():
    defaultConfig = AppConfig("default")
    defaultConfig.showInfo()
    print()
    newConfig = defaultConfig.copyConfig("tonyConfig")
    newConfig.setFontType("雅黑")
    newConfig.setFontSize(18)
    newConfig.setLanguage("English")
    newConfig.showInfo()

testAppConfig()
