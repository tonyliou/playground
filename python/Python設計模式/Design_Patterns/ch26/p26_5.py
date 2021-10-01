# p26_5.py
from p26_4 import TerrestrialAnimal, AquaticAnimal

class Zoo:
    """動物園"""
    def __init__(self):
        self.__animals =[
            TerrestrialAnimal("狗"),
            AquaticAnimal("魚")
        ]
    def displayActivity(self):
        for animal in self.__animals:
            if isinstance(animal, TerrestrialAnimal):
                animal.running()
            else:
                animal.swimming()

zoo = Zoo()
zoo.displayActivity()
