import smtplib

gonderen = "orcun8522@gmail.com"

alici = "orcun8522@gmail.com"

sifre = "mdwrzkwsebvhabiv"

mesaj = "a"

server = smtplib.SMTP("smtp.gmail.com","587")
server.starttls()

server.login(gonderen,sifre)
print("girdin")

server.sendmail(gonderen,alici,mesaj)
print("hata yok")

server.quit()