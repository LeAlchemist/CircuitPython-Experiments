import time
import math
import board
import analogio
import hd44780

potentiometer = analogio.AnalogIn(board.GP26)
potentiometer2 = analogio.AnalogIn(board.GP27)

get_voltage = 3.3 / 65535

display = hd44780.HD44780()

while True:
	voltage = str(math.ceil((potentiometer.value * get_voltage) * 100) / 100)
	voltage2 = str(math.ceil((potentiometer2.value * get_voltage) * 100) / 100)
	print("X " + voltage)
	display.write("X " + voltage, 1)
	print("Y " + voltage2)
	display.write("Y " + voltage2, 2)
	time.sleep(1)