from pyfirmata import Arduino, util
board = Arduino('/dev/ttyACM0')
board.digital[13].write(1)