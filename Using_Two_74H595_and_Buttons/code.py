import board
import busio
import digitalio
import adafruit_74hc595

spi = busio.SPI(board.GP2, board.GP3)
latch_pin = digitalio.DigitalInOut(board.GP1)
sr = adafruit_74hc595.ShiftRegister74HC595(spi, latch_pin, 1)
led = [sr.get_pin(x) for x in range(8)]

spi2 = busio.SPI(board.GP10, board.GP11)
latch_pin2 = digitalio.DigitalInOut(board.GP9)
sr2 = adafruit_74hc595.ShiftRegister74HC595(spi2, latch_pin2, 1)
led2 = [sr2.get_pin(x) for x in range(8)]

pin = [board.GP16, board.GP17, board.GP18, board.GP19, board.GP20]
button = [digitalio.DigitalInOut(pin[x]) for x in range(len(pin))]
for x in range(len(pin)):
    button[x].switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    for x in range(len(button)):
        led[x].value = button[x].value
        led2[x].value = button[x].value & button[4].value