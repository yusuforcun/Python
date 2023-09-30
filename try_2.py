class yazılımcı():
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maaş=maaş
        self.diller=diller
    def bilgilerigoster(self):
        print("""
        yazılımcı objesinin özellikleri :
        isim:{}
        soyisim:{}
        numara:{}
        maaş:{}
        diller:{}
        
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))
    def zamyap(self,zammiktarı):
        print("zam yapılıyor")
        self.maaş+=zammiktarı

    def dilekle(self,diller):
        print("dil ekleniyor")
        self.diller.append(diller)

yazılımcı1=yazılımcı("mustafa0","coskun",64,84650,["python","c","java"])

print(yazılımcı1.bilgilerigoster())

yazılımcı1.zamyap(800)

yazılımcı1.dilekle("sad")
yazılımcı1.bilgilerigoster()