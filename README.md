# FG-GETSET
You can get and set internal properties of an aircraft with the telnet protocol in FlightGear. 

Besides the test file, I added autopilot implementation. The autopilot can control roll degree and vertical speed.

## autopilot usage
`python autopilot_test.py 0 0`

First number sets *roll degree* and second number sets *vertical speed*.

Note: The autopilot implementation has little bit overshoot so if you can find better PID parameters please share with me.
