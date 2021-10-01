# p9_2.py
from os import path
# 引入path，進行路徑相關的處理
import logging
# 引入logging，進行錯誤時的日誌記錄

class ZIPModel:
    """ZIP模組，負責ZIP檔的壓縮與解壓縮
    這裡只進行簡單模擬，不進行具體的解壓縮邏輯"""
    def compress(self, srcFilePath, dstFilePath):
        print("ZIP模組正在進行“%s”檔的壓縮......" % srcFilePath)
        print("檔案壓縮成功，已保存至“%s”" % dstFilePath)
    def decompress(self, srcFilePath, dstFilePath):
        print("ZIP模組正在進行“%s”檔的解壓縮......" % srcFilePath)
        print("檔解壓縮成功，已保存至“%s”" % dstFilePath)

class RARModel:
    """RAR模組，負責RAR檔的壓縮與解壓縮
    這裡只進行簡單模擬，不進行具體的解壓縮邏輯"""
    def compress(self, srcFilePath, dstFilePath):
        print("RAR模組正在進行“%s”檔的壓縮......" % srcFilePath)
        print("檔案壓縮成功，已保存至“%s”" % dstFilePath)
    def decompress(self, srcFilePath, dstFilePath):
        print("RAR模組正在進行“%s”檔的解壓縮......" % srcFilePath)
        print("檔解壓縮成功，已保存至“%s”" % dstFilePath)

class ZModel:
    """7Z模組，負責7Z檔的壓縮與解壓縮
    這裡只進行簡單模擬，不進行具體的解壓縮邏輯"""
    def compress(self, srcFilePath, dstFilePath):
        print("7Z模組正在進行“%s”檔的壓縮......" % srcFilePath)
        print("檔案壓縮成功，已保存至“%s”" % dstFilePath)
    def decompress(self, srcFilePath, dstFilePath):
        print("7Z模組正在進行“%s”檔的解壓縮......" % srcFilePath)
        print("檔解壓縮成功，已保存至“%s”" % dstFilePath)

class CompressionFacade:
    """壓縮系統的外觀類別"""
    def __init__(self):
        self.__zipModel = ZIPModel()
        self.__rarModel = RARModel()
        self.__zModel = ZModel()
    def compress(self, srcFilePath, dstFilePath, type):
        """根據不同的壓縮類型，壓縮成不同的格式"""
        # 獲取新的檔案名
        extName = "." + type
        fullName = dstFilePath + extName
        if (type.lower() == "zip") :
            self.__zipModel.compress(srcFilePath, fullName)
        elif(type.lower() == "rar"):
            self.__rarModel.compress(srcFilePath, fullName)
        elif(type.lower() == "7z"):
            self.__zModel.compress(srcFilePath, fullName)
        else:
            logging.error("Not support this format:" + str(type))
            return False
        return True
    def decompress(self, srcFilePath, dstFilePath):
        """從srcFilePath中獲取尾碼，根據不同的尾碼名(拓展名)，進行不同格式的解壓縮"""
        baseName = path.basename(srcFilePath)
        extName = baseName.split(".")[1]
        if (extName.lower() == "zip") :
            self.__zipModel.decompress(srcFilePath, dstFilePath)
        elif(extName.lower() == "rar"):
            self.__rarModel.decompress(srcFilePath, dstFilePath)
        elif(extName.lower() == "7z"):
            self.__zModel.decompress(srcFilePath, dstFilePath)
        else:
            logging.error("Not support this format:" + str(extName))
            return False
        return True

def testCompression():
    facade = CompressionFacade()
    facade.compress("E:\標準檔\生活中的面板模式.md",
                    "E:\壓縮檔\生活中的面板模式", "zip")
    facade.decompress("E:\壓縮檔\生活中的面板模式.zip",
                      "E:\標準檔\生活中的面板模式.md")
    print()
    facade.compress("E:\標準檔\Python程式設計—從入門到實踐.pdf",
                    "E:\壓縮檔\Python程式設計—從入門到實踐", "rar")
    facade.decompress("E:\壓縮檔\Python程式設計—從入門到實踐.rar",
                      "E:\標準檔\Python程式設計—從入門到實踐.pdf")
    print()
    facade.compress("E:\標準檔\談談我對專案重構的看法.doc",
                    "E:\壓縮檔\談談我對項目重構的看法", "7z")
    facade.decompress("E:\壓縮檔\談談我對項目重構的看法.7z",
                      "E:\標準檔\談談我對專案重構的看法.doc")
    print()

testCompression()
