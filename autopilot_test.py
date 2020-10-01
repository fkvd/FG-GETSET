"""
Autopilot implementation for FlightGear.
It can only control roll degree and
vertical speed by using PID.

Since system has little bit overshoot,
you might want to change PID parameters.

@fkvd		24.09.2020

"""

from telnetlib import Telnet
from getsetFG import *
from pid import *
import sys

tnGET = Telnet("localhost",7777)
tnSET = Telnet("localhost",7777)

VERTICAL_SPEED = 0
ROLL_DEGREE    = 0

try:
	ROLL_DEGREE = float(sys.argv[1])
	VERTICAL_SPEED = float(sys.argv[2])
except:
	pass


VERTICAL_SPEED = VERTICAL_SPEED*1.6667 # Conversion to FEET PER MIN

tune = 0.002
pidE = PID(2*tune, tune/2, tune/4, setpoint=VERTICAL_SPEED)
pidR = PID(4*tune, tune/2, tune/1, setpoint=ROLL_DEGREE)

while True:
	v = getVerticalSpeed(tnGET)
	controlE = pidE.update(v)
	r = getRoll(tnGET)
	controlR = pidR.update(r)
	
	if(controlE>0.3):
		controlE = 0.3
	elif(controlE<-0.3):
		controlE = -0.3
	setElevator(tnSET, -1*controlE)


	if(controlR>0.20):
		controlR = 0.20
	elif(controlR<-0.20):
		controlR = -0.20
	setAileron(tnSET, controlR)

