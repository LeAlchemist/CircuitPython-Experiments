import time
import board
import busio
import digitalio
import adafruit_74hc595

spi = busio.SPI(board.GP2, board.GP3)
latch_pin = digitalio.DigitalInOut(board.GP0)
sr = adafruit_74hc595.ShiftRegister74HC595(spi, latch_pin, 1)

led0 = sr.get_pin(0)
led1 = sr.get_pin(1)
led2 = sr.get_pin(2)

while True:
    led0.value = True
    led2.value = False
    time.sleep(1)
    led0.value = False
    led1.value = True
    time.sleep(1)
    led1.value = False
    led2.value = True
    time.sleep(1)