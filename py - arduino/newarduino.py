from pyfirmata import Arduino, util, STRING_DATA
import time
import serial
import tkinter 


board = Arduino("COM3")

# board.send_sysex( STRING_DATA, util.str_to_two_byte_iter('Hello!') )

# def msg( text ):
#     if text:
#         board.send_sysex( STRING_DATA, util.str_to_two_byte_iter( text ) )
        

ser = serial.Serial('/dev/ttyUSB3',9600)
ser.write("fders")


# led = board.get_pin('d:13:o')

# # board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("merhaba") )
# while True :
#     led.write(1) 
#     # msg("led opened")
#     time.sleep(8)
#     led.write(0)
#     # msg("led off")
#     time.sleep(2)