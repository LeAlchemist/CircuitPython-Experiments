import time
import board
import digitalio
import hd44780

button = digitalio.DigitalInOut(board.GP2)
button.switch_to_input(pull=digitalio.Pull.DOWN)

display = hd44780.HD44780()

while True:
	display.clear()
	print(button.value)
	display.write("Button: " + str(button.value), 1)
	time.sleep(1)