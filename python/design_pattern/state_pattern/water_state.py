from abc import ABCMeta, abstractmethod

class Water:
	def __init__ (self, state):
		self._temperature = 25
		self._state = state
	
	def setState(self, state):
		self._state = state
	
	def changeState(self, state):
		if (self._state):
			print("由", self._state.getName(), "變為", state.getName())
		
		else:
			print("初始化為", state.getName())
		self._state = state
	
	def getTemperature(self):
		return self._temperature
	
	def setTemperature(self, temperature):
		self._temperature = temperature
		if (self._temperature <= 0):
			self.changeState(SolidState("固態"))
		
		elif (self._temperature <= 100):
			self.changeState(LiquidState("液態"))
		
		else:
			self.changeState(GaseousState("氣態"))
	
	def riseTemperature(self, step):
		self.setTemperature(self._temperature + step)
	
	def reduceTemperature(self, step):
		self.setTemperature(self._temperature - step)
	
	def behavior(self):
		self._state.behavior(self)

class State(metaclass=ABCMeta):
	def __init__(self, name):
		self._name = name
	
	def getName(self):
		return self._name
	
	def behavior(self, water):
		pass

class SolidState(State):
	def __init__(self, name):
		super().__init__(name)

	def behavior(self, water):
		print("我是冰，當前溫度" + str(water.getTemperature()))
	
class LiquidState(State):
	def __init__(self, name):
		super().__init__(name)

	def behavior(self, water):
		print("我是水，當前溫度" + str(water.getTemperature()))

class GaseousState(State):
	def __init__(self, name):
		super().__init__(name)

	def behavior(self, water):
		print("我是氣體，當前溫度" + str(water.getTemperature()))

def testState():
	water = Water(LiquidState("液態"))
	water.behavior()
	water.setTemperature(-4)
	water.behavior()
	water.riseTemperature(18)	
	water.behavior()
	water.riseTemperature(110)
	water.behavior()

testState()
