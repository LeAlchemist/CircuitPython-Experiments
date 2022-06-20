import board
import neopixel
import time

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
x = 0
y = 0
z = 0

while True:
    led.fill((x, y, z))
    x = x + 1
    print(str(x) + " " + str(y) + " " + str(z))

    if x >= 255:
        x = 0
        y = y + 1
    
    if y >= 255:
        y = 0
        z = z + 1

    if z >= 255:
        z = 0