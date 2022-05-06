import microcontroller
import time

while True:
	temp = microcontroller.cpu.temperature
	print("Temp is")
	tempC = str(round(temp)) + "° C"
	print(tempC)
	tempF = str(round(temp * (9/5) + 32)) + "˚ F"
	print(tempF)
	time.sleep(1)