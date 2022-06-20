import board
import busio
import digitalio
import adafruit_74hc595

spi = busio.SPI(board.GP2, board.GP3)
latch_pin = digitalio.DigitalInOut(board.GP0)
sr = adafruit_74hc595.ShiftRegister74HC595(spi, latch_pin, 1)
led = [sr.get_pin(x) for x in range(8)]

pin = [board.GP6, board.GP7, board.GP8]
button = [digitalio.DigitalInOut(pin[x]) for x in range(len(pin))]
for x in range(len(pin)):
    button[x].switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    for x in range(len(button)):
        led[x].value = button[x].value