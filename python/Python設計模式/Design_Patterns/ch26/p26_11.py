# p26_11.py
import os
# 導入os庫，用於檔、路徑相關的解析

def getPath(basePath, fileName):
    extName = os.path.splitext(fileName)[1]
    filePath = basePath
    if(extName.lower() == ".txt"):
        filePath += "/txt/"
    elif(extName.lower() == ".pdf"):
        filePath += "/pdf/"
    else:
        filePath += "/other/"
    # 如果目錄不存在，則創建新目錄
    if (not os.path.exists(filePath)):
        os.makedirs(filePath)
    filePath += fileName
    return filePath
