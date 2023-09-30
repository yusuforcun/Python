import smtplib #kütüphaneyi import ettik
    

toplammail=3 #kaç mail atacagız onun sayısı biz giriyoruz

# sirketadi = ['Sirket1', 'Sirket2', 'Sirket3'] #sirket gmailleri 
isim=["Esma Dilek","Dilek AŞKAR","Nurgül İpek"]  #gmailde kullanılacak isim

sirketmailleri=["talhabagcecik@gmail.com","askard@uib.org.tr","nurgul@tosfed.org.tr"] #mailimizdeki şirketin gmail adresi


x=0 #döngü için sıfırdan baslıyor

mail = smtplib.SMTP("smtp.gmail.com",587) #mail sunucusu 

# mesaj=f"Sayın  {isim[x]}   " 

mail.starttls() 
while x<toplammail:  #döngü baslangıcı :

    content=(f"Merhabalar {isim[x]} Ben Moon Star Robotics takım kaptanı Eyüp. 27-28-29 Mart tarihlerinde gerçekleşen Bosphorus Regional yarışmasında Quality ödülü aldık, takımımla beraber şampiyonluk elde ettik ve Dünya Şampiyonasına gitmeye hak kazandık. Fakat bizden salı gününe kadar başvuru ücreti olarak 5000 dolar isteniyor. Takım olarak bu parayı birçok yerden karşılamaya çalışıyoruz. Bu konuda elinizden geldiğince bize yardımcı olabilir misiniz?") 
    content = content.encode('utf-8')
    mail.ehlo() 
    
    mail.login("orcun8522@gmail.com","mdwrzkwsebvhabiv") #hesaba giris
    gmail=sirketmailleri[x]
    send="orcun8522@gmail.com"
    mail.sendmail(send,gmail,content)  #mail gönderme
    
    x+=1 #tur sayısını yazar ama bir eksiktir degiskeni x oldugu için
  

    


