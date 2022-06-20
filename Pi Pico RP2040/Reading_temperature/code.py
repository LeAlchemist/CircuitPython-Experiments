import microcontroller
import time
import board
import hd44780

display = hd44780.HD44780()

#temperature readout
while True:
	temp = microcontroller.cpu.temperature
	display.write ("CPU Temp is:", 1)
	tempC = str(round(temp)) + " C"
	print(tempC)
	tempF = str(round(temp * (9/5) + 32)) + " F"
	print(tempF)
	display.write (tempC + " " + tempF, 2)
	time.sleep(1)