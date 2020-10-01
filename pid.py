"""
@fkvd	27.09.2020

"""

import time

class PID:

	def __init__(self, Kp, Ki, Kd, setpoint):
		self.__Kp = Kp
		self.__Ki = Ki
		self.__Kd = Kd
		self.__setpoint = setpoint
		self.__previousError = 0
		self.__previousMeasurement = 0
		self.__previousTime = None
		self.__integralSum = 0

	def show(self):
		print("Kp: " + str(self.__Kp))
		print("Ki: " + str(self.__Ki))
		print("Kd: " + str(self.__Kd))
		print("sp: " + str(self.__setpoint))

	def update(self, measurement):
		error = self.__setpoint - measurement

		if self.__previousTime is None:
			timeDifference = 0.1
			self.__previousError = time.clock()
		else:
			timeDifference = time.clock() - self.__previousTime

		P = self.__Kp * error
		self.__integralSum += self.__Ki * error * timeDifference
		D = -self.__Kd * (measurement - self.__previousMeasurement) / timeDifference

		self.__previousTime = time.clock()
		self.__previousError = error

		return P + self.__integralSum + D