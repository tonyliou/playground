# p22_2.py
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法
import logging
# 引入logging模組用於輸出日誌資訊
import time
# 引入時間模組
logging.basicConfig(level=logging.INFO)
# 如果想在控制台列印INFO以上的資訊，則加上此配製

class PooledObject:
    """池物件,也稱池化對象"""
    def __init__(self, obj):
        self.__obj = obj
        self.__busy = False
    def getObject(self):
        return self.__obj
    def setObject(self, obj):
        self.__obj = obj
    def isBusy(self):
        return self.__busy
    def setBusy(self, busy):
        self.__busy = busy

class ObjectPool(metaclass=ABCMeta):
    """物件集區"""
    """物件集區初始化大小"""
    InitialNumOfObjects = 10
    """物件集區最大的大小"""
    MaxNumOfObjects = 50
    def __init__(self):
        self.__pools = []
        for i in range(0, ObjectPool.InitialNumOfObjects):
            obj = self.createPooledObject()
            self.__pools.append(obj)
    @abstractmethod
    def createPooledObject(self):
        """創建池物件, 由子類實現該方法"""
        pass
    def borrowObject(self):
        """借用對象"""
        # 如果找到空閒物件，直接返回
        obj = self._findFreeObject()
        if(obj is not None):
            logging.info("%x對象已被借用, time:%s", id(obj),
                         time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
            return obj
        # 如果物件集區未滿，則添加新的物件
        if(len(self.__pools) < ObjectPool.MaxNumOfObjects):
            pooledObj = self.addObject()
            if (pooledObj is not None):
                pooledObj.setBusy(True)
                logging.info("%x對象已被借用, time:%s", id(obj),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
                return pooledObj.getObject()
        # 物件集區已滿且沒有空閒物件，則返回None
        return None
    def returnObject(self, obj):
        """歸還對象"""
        for pooledObj in self.__pools:
            if(pooledObj.getObject() == obj):
                pooledObj.setBusy(False)
                logging.info("%x對象已歸還, time:%s", id(obj),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
                break
    def addObject(self):
        """添加新對象"""
        obj = None
        if(len(self.__pools) < ObjectPool.MaxNumOfObjects):
            obj = self.createPooledObject()
            self.__pools.append(obj)
            logging.info("添加新對象%x, time:", id(obj),
                         time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
        return obj
    def clear(self):
        """清空物件集區"""
        self.__pools.clear()
    def _findFreeObject(self):
        """查找空閒的對象"""
        obj = None
        for pooledObj in self.__pools:
            if(not pooledObj.isBusy()):
                obj = pooledObj.getObject()
                pooledObj.setBusy(True)
                break
        return obj
