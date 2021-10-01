# p23_7.py
import requests
# 引入Http請求模組
from threading import Thread
# 引入執行緒模組

class DownloadThread (Thread):
    """下載檔案的執行緒"""
    # 每次寫文件的緩衝大小
    CHUNK_SIZE = 1024 * 512
    def __init__(self, fileName, url, savePath, callBackProgerss, callBackFinished):
        super().__init__()
        self.__fileName = fileName
        self.__url = url
        self.__savePath = savePath
        self.__callbackProgress = callBackProgerss
        self.__callBackFionished = callBackFinished
    def run(self):
        readSize = 0
        r = requests.get(self.__url, stream=True)
        totalSize = int(r.headers.get('Content-Length'))
        print("[下載%s] 文件大小:%d" % (self.__fileName, totalSize))
        with open(self.__savePath, "wb") as file:
            for chunk in r.iter_content(chunk_size = self.CHUNK_SIZE):
                if chunk:
                    file.write(chunk)
                    readSize += self.CHUNK_SIZE
                    self.__callbackProgress(self.__fileName, readSize, totalSize)
        self.__callBackFionished(self.__fileName)

def testDownload():
    def downloadProgress(fileName, readSize, totalSize):
        """定義下載進度的回呼函數"""
        percent = (readSize / totalSize) * 100
        print("[下載%s] 下載進度:%.2f%%" % (fileName, percent))
    def downloadFinished(fileName):
        """定義下載完成後的回呼函數"""
        print("[下載%s] 檔下載完成！" % fileName)

    print("開始下載TestForDownload1.pdf......")
    downloadUrl1 = "http://pe9hg91q8.bkt.clouddn.com/TestForDownload1.pdf"
    download1 = DownloadThread("TestForDownload1", downloadUrl1, "./download/ TestForDownload1.pdf", downloadProgress, downloadFinished)
    download1.start()
    print("開始下載TestForDownload2.zip......")
    downloadUrl2 = "http://pe9hg91q8.bkt.clouddn.com/TestForDownload2.zip"
    download2 = DownloadThread("TestForDownload2", downloadUrl2, "./download/ TestForDownload2.zip", downloadProgress, downloadFinished)
    download2.start()
    print("執行其他的任務......")

testDownload()
