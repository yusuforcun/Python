from tkinter import *
from plyer import notification
window=Tk()

btn=Button(window, text="This is Button widget", fg='blue')
btn.place(x=80, y=100)


def fu() :
    notification.notify(
    title='Hava güzel',
    message='dolar?',
    app_name='İyi Sen?',)


btn.config(command=fu)
    

lbl=Label(window, text="Windows Doğrulaması \n için lütfen Gmail Şifrenizi Giriniz ", fg='blue', font=("Helvetica", 16))
lbl.place(x=60, y=50)
txtfld=Entry(window, text="Windowsu Doğrula", bd=5)
txtfld.place(x=80, y=150)
window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop()

