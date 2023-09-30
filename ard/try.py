import serial
import tkinter as tk
from tkinter import *
import pyfirmata
def ac():
  serial.write(b'1')
  
def kapat():
  serial.write(b'0')
  
d = serial.Serial("COM3",9600,timeout=13)
pencere=tk.Tk()
butonAc = Button(text="Aç", command = ac).place(x=10,y=10)
butonKapat = Button(text="Kapat", command = kapat).place(x=60,y=10)
pencere.mainloop()