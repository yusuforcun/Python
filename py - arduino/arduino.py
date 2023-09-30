from pyfirmata import Arduino 
import time
board = Arduino('COM')

led = board.get_pin('d:13:o')

while True:
    led.write("LOW")
    time.sleep(5)
    led.write("HIGH")
    time.sleep(1)