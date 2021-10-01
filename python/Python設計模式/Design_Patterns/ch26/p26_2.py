# p26_2.py
class Animal:
    """動物"""
    def __init__(self, name, type):
        self.__name = name
        self.__type = type
    def running(self):
        if(self.__type == "水生"):
            print(self.__name + "在水裡遊...")
        else:
            print(self.__name + "在陸上跑...")

Animal("狗", "陸生").running()
Animal("魚", "水生").running()
