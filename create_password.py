import math
import random
import string

mesaj = input("mesajınızı giriniz: ")
kullanilicaklar = "abcçdefgğhıijklmnoöprsştuüvyzqwx"

boyutal = len(kullanilicaklar)
sifreli_mesaj = ""

print("mesaj: ", mesaj)

for i in mesaj:
    for a in kullanilicaklar:
        if i == a:
            konum = kullanilicaklar.index(a)
            
            konum+=8
            sifreli_mesaj += kullanilicaklar[konum % boyutal]

a = "nLgX629b3KJZq78imH92fYORPoGxWlrBM6K1VuzCnjgXNt4AU0wcQseLFd5bIvk3TEpayShDkvAJYHC1pIaqyBtGhTcxFwrjfi4w04MHYcv3LyrsTI5gaWbE1JX9uAjC6DeoGFtOqUdflKmQkznNpi2RVZh78SxBPDEUZseuVd0WPS75lMzmNo8OQR"
a = list(a)
random.shuffle(a)
random.shuffle(a)
metin = ""
for r in a:
    metin+=r

islem=""
for x in metin:
    islem=islem+x


islem=list(islem)
# print(islem)
islem2=""
for t in islem:
    islem2+=t
# print(islem2)
sifreli_mesaj+=islem2

print("şifreli mesaj: ", sifreli_mesaj[:100])

sifre=open("sifre.txt","a",encoding="utf-8")
sifre.write(sifreli_mesaj)
sifre.close()