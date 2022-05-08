import time
import board
import analogio
import hd44780

potentiometer = analogio.AnalogIn(board.GP26)

get_voltage = 3.3 / 65535

display = hd44780.HD44780()

while True:
	voltage = str(potentiometer.value * get_voltage)
	print(voltage)
	display.write(voltage, 1)
	time.sleep(2)