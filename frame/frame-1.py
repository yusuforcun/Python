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

hatırlatma_tipi_etiket = Label(upper_frame , bg='#add8e6' , text="Hatırlatma tipi :",font="Verdana 12 bold")
hatırlatma_tipi_etiket.pack(padx=10,pady=10,side=LEFT)

hatırlatma_tipi_opsiyon = StringVar(upper_frame)
hatırlatma_tipi_opsiyon.set("\t")

hatırlatma_tipi_acilir_menu = OptionMenu(
   upper_frame,
   hatırlatma_tipi_opsiyon,
   "Doğum günü",
   "alışveriş",
   "ödeme")

hatırlatma_tipi_acilir_menu.pack(padx=10,pady=10,side=LEFT) 

#hatırlatma_tarih_secici =DateEntry(upper_frame , width=12 ,background='orange' , foreground="black" , borderwidth=1 ,locale ="de_DE")
#hatırlatma_tarih_secici._top_cal_overrideredirect(False)
#hatırlatma_tarih_secici.pack(padx=10,pady=10,side=RIGHT)

hatırlatma_tarih_etiket = Label(upper_frame,bg='#add8e6',text="Hatırlatma tarihi : ",fond=("Verdana 12 bold"))
hatırlatma_tarih_etiket.pack(padx=10,pady=10,side=RIGHT)

master.mainloop()