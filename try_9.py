#banka uygulaması yapıyoruz
#bankacının adı ,hesap numarası,parası,mesleği girilsin gerektiğinde değiştirilsin.

class bankuser():
        def __init__(self,name="not logined",number="not logined",job="not logined"):
            self.name=name
            self.number=number
            self.job=job

user1=bankuser(name="lfsd",job="vkml")

print(user1.name)
print(user1.number)
print(user1.job) 
