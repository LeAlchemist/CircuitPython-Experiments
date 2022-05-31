import time
import board
import busio
import digitalio
import adafruit_mcp3xxx.mcp3008
from adafruit_mcp3xxx.analog_in import AnalogIn

#define MCP0
spi0 = busio.SPI(clock= board.GP2, MOSI= board.GP3, MISO= board.GP4)
cs0 = digitalio.DigitalInOut(board.GP5)
MCP0 = adafruit_mcp3xxx.mcp3008
mcp0 = MCP0.MCP3008(spi0, cs0)
#MCP0 pin output
mcp0_pin = [AnalogIn(mcp0, MCP0.P0), AnalogIn(mcp0, MCP0.P1)]

while True:
    pmeter_output = [mcp0_pin[0], mcp0_pin[1]]
    for x in range(len(mcp0_pin)):
        if mcp0_pin[x].voltage < (3.3/2): #convert value range to -1 - 0
            pmeter_output[x] = ((mcp0_pin[x].voltage - (3.3/2)) / (3.3/2))
        else: #convert value range to 0 - 1
            pmeter_output[x] = ((mcp0_pin[x].voltage - (3.3/2)) / (3.3/2))

    print("0: ", pmeter_output[0], " 1: ", pmeter_output[1])
    time.sleep(1)