import os
from p11_2 import Component, Composite
# 引入 os 模組

class FileDetail(Component):
    """文件詳情"""
    def __init__(self, name):
        super().__init__(name)
        self._size = 0
    def setSize(self, size):
        self._size = size
    def getFileSize(self):
        return self._size
    def feature(self, indent):
        # 檔大小，單位：KB，精確度：2位小數
        fileSize = round(self._size / float(1024), 2)
        print("檔案名稱：%s， 文件大小：%sKB" % (self._name, fileSize) )

class FolderDetail(Composite):
    """資料夾詳情"""
    def __init__(self, name):
        super().__init__(name)
        self._count = 0
    def setCount(self, fileNum):
        self._count = fileNum
    def getCount(self):
        return self._count
    def feature(self, indent):
        print("資料夾名：%s， 檔數量：%d。包含的檔：" % (self._name, self._count) )
        super().feature(indent)

def scanDir(rootPath, folderDetail):
    """掃描某一資料夾下的所有目錄"""
    if not os.path.isdir(rootPath):
        raise ValueError("rootPath不是有效的路徑：%s" % rootPath)
    if folderDetail is None:
        raise ValueError("folderDetail不能為空!")

    fileNames = os.listdir(rootPath)
    for fileName in fileNames:
        filePath = os.path.join(rootPath, fileName)
        if os.path.isdir(filePath):
            folder = FolderDetail(fileName)
            scanDir(filePath, folder)
            folderDetail.addComponent(folder)
        else:
            fileDetail = FileDetail(fileName)
            fileDetail.setSize(os.path.getsize(filePath))
            folderDetail.addComponent(fileDetail)
            folderDetail.setCount(folderDetail.getCount() + 1)

def testDir():
    folder = FolderDetail("生活中的設計模式")
    scanDir("D:\Design_Patterns\ch11\生活中的設計模式", folder)
    folder.feature("")

testDir()
