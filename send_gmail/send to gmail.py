from distutils import config
import smtplib
import time #kütüphaneyi import ettik
x=0 #döngü için sıfırdan baslıyor

toplammail=3 #kaç mail atacagız onun sayısı biz giriyoruz

isimmailleri=["None","sdvjsm","ıjsdovoıjok"]  #mailimizdeki ad
sirketmailleri=["beyyusuf009@gmail.com","beyyusuf009@gmail.com","beyyusuf009@gmail.com"] #mailimizdeki şirketin gmail adresi

mail = smtplib.SMTP("smtp.gmail.com",587) #mail sunucusu
print("sunucuya baglandı") 
time.sleep(1)

while x<=toplammail:  #döngü baslangıcı :
        
        content=f"merhaba  {isimmailleri}  \numarım iyisinizdir" 

        mail.ehlo() #kendimizi tanıttık büyük ihtimal
        print("ehlo calıstı")
        time.sleep(1)
        mail.starttls() #tam bilmitorum
        print(toplammail,isimmailleri,sirketmailleri)
        time.sleep(1)
        mail.login("orcun8522@gmail.com","27982798Yo") #hesaba giris
        print("hesaba girdik")
        time.sleep(1)
        mail.sendmail("orcun8522@gmail.com",sirketmailleri,content)  #mail gönderme
        print("tur ",x)  #tur sayısını yazar ama bir eksiktir degiskeni x oldugu için
        x=x+1  #sonsuz loop olmaması için şirket gmaili için

