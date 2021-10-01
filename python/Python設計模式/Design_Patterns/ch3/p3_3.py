# p3_3.py
# 基於框架的實現
#==============================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod來定義抽象類別和抽象方法
from enum import Enum
# Python 3.4之後支援枚舉Enum的語法

class DeviceType(Enum):
    "設備類型"
    TypeSpeaker = 1
    TypeMicrophone = 2
    TypeCamera = 3

class DeviceItem:
    """設備項"""
    def __init__(self, id, name, type, isDefault = False):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__isDefault = isDefault
    def __str__(self):
        return "type:" + str(self.__type) + " id:" + str(self.__id) \
               + " name:" + str(self.__name) + " isDefault:" + str(self.__isDefault)
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getType(self):
        return self.__type
    def isDefault(self):
        return self.__isDefault

class DeviceList:
    """設備清單"""
    def __init__(self):
        self.__devices = []
    def add(self, deviceItem):
        self.__devices.append(deviceItem)
    def getCount(self):
        return len(self.__devices)
    def getByIdx(self, idx):
        if idx < 0 or idx >= self.getCount():
            return None
        return self.__devices[idx]
    def getById(self, id):
        for item in self.__devices:
            if( item.getId() == id):
                return item
        return None

class DeviceMgr(metaclass=ABCMeta):
    @abstractmethod
    def enumerate(self):
        """枚舉設備清單
        (在程式初始化時，有設備插拔時都要重新獲取設備清單)"""
        pass
    @abstractmethod
    def active(self, deviceId):
        """選擇要使用的設備"""
        pass
    @abstractmethod
    def getCurDeviceId(self):
        """獲取當前正在使用的設備ID"""
        pass

class SpeakerMgr(DeviceMgr):
    """揚聲器設備管理類"""
    def __init__(self):
        self.__curDeviceId = None
    def enumerate(self):
        """枚舉設備清單
        (真實的專案應該通過驅動程式去讀取設備資訊，這裡只用初始化來模擬)"""
        devices = DeviceList()
        devices.add(DeviceItem("369dd760-893b-4fe0-89b1-671eca0f0224", "Realtek High Definition Audio", DeviceType.TypeSpeaker))
        devices.add(DeviceItem("59357639-6a43-4b79-8184-f79aed9a0dfc", "NVIDIA High Definition Audio", DeviceType.TypeSpeaker, True))
        return devices
    def active(self, deviceId):
        """啟動指定的設備作為當前要用的設備"""
        self.__curDeviceId = deviceId
    def getCurDeviceId(self):
        return self.__curDeviceId

class DeviceUtil:
    """設備工具類"""

    def __init__(self):
        self.__mgrs = {}
        self.__mgrs[DeviceType.TypeSpeaker] = SpeakerMgr()
        # 為節省篇幅，MicrophoneMgr和CameraMgr不再實現
        # self.__microphoneMgr = MicrophoneMgr()
        # self.__cameraMgr = CameraMgr
    def __getDeviceMgr(self, type):
        return self.__mgrs[type]
    def getDeviceList(self, type):
        return self.__getDeviceMgr(type).enumerate()
    def active(self, type, deviceId):
        self.__getDeviceMgr(type).active(deviceId)
    def getCurDeviceId(self, type):
        return self.__getDeviceMgr(type).getCurDeviceId()

def testDevices():
    deviceUtil = DeviceUtil()
    deviceList = deviceUtil.getDeviceList(DeviceType.TypeSpeaker)
    print("麥克風設備清單：")
    if deviceList.getCount() > 0:
        # 設置第一個設備為要用的設備
        deviceUtil.active(DeviceType.TypeSpeaker, deviceList.getByIdx(0).getId())
    for idx in range(0, deviceList.getCount()):
        device = deviceList.getByIdx(idx)
        print(device)
    print("當前使用的設備："
          + deviceList.getById(deviceUtil.getCurDeviceId(DeviceType.TypeSpeaker)). getName())

testDevices()

