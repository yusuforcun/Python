from doctest import master
from tkinter import *

master=Tk()

canvas=Canvas(master , height=450 , width=750)
canvas.pack

upper_frame=Frame(master , bg='#add8e6')
upper_frame.place(relx=0.1 , rely=0.1 ,relwidth=0.8 ,relheight=0.1)

subframe=Frame(master , bg='#add8e6')
subframe.place(relx=0.1 , rely=0.21 ,relwidth=0.23 ,relheight=0.5)

right_frame=Frame(master , bg='#add8e6')
right_frame.place(relx=0.34 , rely=0.21 ,relwidth=0.56 ,relheight=0.5)

master.mainloop()