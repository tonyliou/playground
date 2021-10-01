class Observer:
    "觀察者的基類"
    def update(self, observer, object):
        pass


class Observable:
    "被觀察者的基類"
    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, object = 0):
        for o in self.__observers:
            o.update(self, object)


class WaterHeater(Observable):
    "熱水器：戰勝寒冬的有利武器"
    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("current temperature is:", self.__temperature)
        self.notifyObservers()


class WashingMode(Observer):
    "該模式用於洗澡用"
    def update(self, observable, object):
        if isinstance(observable,
                      WaterHeater) and observable.getTemperature() >= 50 and observable.getTemperature() < 70:
            print("水已燒好，溫度正好！可以用來洗澡了。")


class DrinkingMode(Observer):
    "該模式用於飲用"
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
            print("水已燒開！可以用來飲用了。")

heater = WaterHeater()
washingObser = WashingMode()
drinkingObser = DrinkingMode()
heater.addObserver(washingObser)
heater.addObserver(drinkingObser)
heater.setTemperature(40)
heater.setTemperature(60)
heater.setTemperature(100)
