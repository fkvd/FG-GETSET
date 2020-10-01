"""
You can test getsetFG.py

@fkvd		24.09.2020

"""
from telnetlib import Telnet
from getsetFG import *

# Two different telnet object must be
# created. Otherwise it won't work.
tnGET = Telnet("localhost",7777)
tnSET = Telnet("localhost",7777)

altitude = str(getAltitude(tnGET))
aileron  = str(getManual(tnGET, "controls/flight/aileron"))
elevator = str(getManual(tnGET, "controls/flight/elevator"))
flapsSer = str(getManual(tnGET, "controls/flight/flaps-serviceable", "bool"))
print("altitude: " + altitude)
print("aileron: " + aileron)
print("elevator: " + elevator)
print("flaps-serviceable: " + flapsSer)


while(True):
	getsetTEST(tnSET)



	


