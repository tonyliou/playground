# p26_12.py
import os
# 導入os庫，用於檔、路徑相關的解析

def getPath(basePath, fileName):
    extName = fileName.split(".")[1]
    filePath = basePath + "/" + extName + "/"
    # 如果目錄不存在，則創建新目錄
    if (not os.path.exists(filePath)):
        os.makedirs(filePath)
    filePath += fileName
    return filePath
