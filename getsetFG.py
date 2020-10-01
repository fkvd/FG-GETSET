"""
You can easily get and set internal
properties of any aircraft in FlightGear.

@fkvd		24.09.2020				

""" 
									
import re
import time

# Manually get and set double or boolean 
# value by using regular expression
def getManual(tnGET, command, varType="double"):
	commandStr = "get " + command + "\r\n"
	tnGET.write(commandStr.encode())
	varTypeStr = "(" + varType + ")"
	data = tnGET.read_until(varTypeStr.encode())
	decodedData = data.decode('utf-8')
						
	lastSlashIndex = command.rindex("/")
	element = command[lastSlashIndex+1:]

	try:
		if(decodedData.count(element)):
			if(varType=="double"):
				try:
					extractedData = float((re.findall("-?\d+\.\d+", decodedData))[0])
					return extractedData
				except:
					return 0
			elif(varType=="bool"):
				extractedData = (re.findall("(?:^|\s)'([^']*?)'(?:$|\s)", decodedData))[0]
				return extractedData
	except:
		print("Error Occured")
		return -9999


def setManual(tnSET, command, value):
	commandStr = "set " + command + " " + str(value) + "\r\n"
	tnSET.write(bytes(commandStr,'utf-8'))



# Automatic Get and Set Functions

def getAltitude(tnGET):
	return getManual(tnGET, "position/altitude-ft")

def getVerticalSpeed(tnGET):
	return getManual(tnGET, "velocities/vertical-speed-fps")

def getElevator(tnGET):
	return getManual(tnGET, "controls/flight/elevator")

def getRoll(tnGET):
	return getManual(tnGET, "orientation/roll-deg")

def getThrottle(tnGET):
	return getManual(tnGET,"controls/engines/current-engine")

def getRudder(tnGET):
	return getManual(tnGET, "controls/flight/rudder")



def setElevator(tnSET, value):
	setManual(tnSET, "controls/flight/elevator", value)

def setAileron(tnSET, value):
	setManual(tnSET, "controls/flight/aileron", value)

def setThrottle(tnSET, value):
	setManual(tnSET, "controls/engines/current-engine", value)

def setRudder(tnSET, value):
	setManual(tnSET, "controls/flight/rudder", value)



# getsetTest Function
def getsetTEST(tnSET, sleepTime = 1):

	setElevator(tnSET, -1.0)
	time.sleep(sleepTime)
	setElevator(tnSET, 1.0)
	time.sleep(sleepTime)
	setElevator(tnSET, 0)
	time.sleep(sleepTime)

	setAileron(tnSET, -1.0)
	time.sleep(sleepTime)
	setAileron(tnSET, 1.0)
	time.sleep(sleepTime)
	setAileron(tnSET, 0)
	time.sleep(sleepTime)

	setRudder(tnSET, -1.0)
	time.sleep(sleepTime)
	setRudder(tnSET, 1.0)
	time.sleep(sleepTime)
	setRudder(tnSET, 0.0)
	time.sleep(sleepTime)

