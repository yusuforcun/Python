from doctest import master
from tkinter import *
from tkinter import font

master=Tk()

canvas=Canvas(master , height=9000000 , width=9000)
canvas.pack

subframe=Frame(master , bg='#add8e6')
subframe.place(relx=0.1 , rely=0.21 ,relwidth=0.23 ,relheight=0.5)

metin=Text(subframe,height=9,width=50)
metin.tag_configure("style",foreground="#bfbfbf",font=("Verdana",7,"bold"))
metin.pack()
metin =str(metin)
def kaydet():
    dosya = open("saksak", "w")
    dosya.write(metin)
    dosya.close()

buton=Button(subframe , text="gönder")

kaydet()
master.mainloop()