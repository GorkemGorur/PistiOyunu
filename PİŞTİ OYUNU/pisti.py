import random as rnd
class deste:
	def __init__(self):
		self.turler = ('Karo','Kupa','Maça','Sinek')
		self.sayilar = tuple(['A']+[str(x) for x in range(2,11)]+['J','Q','K'])
		self.destem = []
		self.kart_sayisi = 52
		self.olustur()
		self.karistir()
		self.kes()

	def olustur(self):
		self.destem = [tur+sayi for tur in self.turler for sayi in self.sayilar]
		#print(self.destem)

	def karistir1(self):
		bosliste = []
		for x in range(self.kart_sayisi):
			"""
			rastgele = rnd.randint(0,len(self.destem))
			bosliste.append(self.destem[rastgele])
			self.destem.pop(rastgele)
			"""
			bosliste.append(self.destem.pop(rnd.randint(0,len(self.destem)-1)))
		self.destem = bosliste
		#print(self.destem)
	
	def karistir(self):
		self.destem = rnd.sample(self.destem,self.kart_sayisi)
		#print(self.destem)

	def kes(self):
		rastgele = rnd.randint(0,self.kart_sayisi-1)
		self.destem = self.destem[rastgele+1:]+self.destem[:rastgele+1]
		#print(self.destem)

	def dagit1(self, adet = 1):
		bos = []
		for tekrar in range(adet):
			bos.append(self.destem.pop(0))
		return bos

	def dagit(self,adet=1):
		return [self.destem.pop(0) for tekrar in range(adet)]

class oyuncu:
	def __init__(self, ad):
		self.ad = ad
		self.kartlar = []
		self.puan = 0
		self.pisti = 0
		self.toplanan_kartlar = []
		self.oyuncu_sira = 0

	def kart_at(self, adet = 1):
		return [self.kartlar.pop(0) for tekrar in range(adet)] # en üstteki kart/ları atar
		#return [self.kartlar.pop(rnd.randint(0,len(self.kartlar)-1)) for tekrar in range(adet)]#rastgele kartları atar

isimler = ['Ali','Veli','Ayşe','Fatma','Yer']
#oyuncu1 = oyuncu('Ali')

"""
oyuncular = []
for isim in isimler:
	oyuncular.append(oyuncu(isim))
"""

oyuncular = [oyuncu(isim) for isim in isimler]

iskambil = deste()

for oyuncu in oyuncular:
	oyuncu.kartlar = iskambil.dagit(4)

enusttekikart = oyuncular[4].kartlar[0]


while oyuncular[3].kartlar:

	while oyuncular[3].kartlar:  #len(oyuncular[3].kartlar)>0		
		for sira,oyuncu in enumerate(oyuncular[:4]):			
			atilan = oyuncu.kart_at()
			oyuncular[4].kartlar.extend(atilan)
			if atilan == enusttekikart:
				ensonalan = sira
				if len(oyuncular[4].kartlar)==2:
					oyuncu.pisti += 1
					oyuncu.toplanan_kartlar.extend(oyuncular[4].kartlar)
					oyuncular[4].kartlar.clear()
					enusttekikart = ''
				else:
					oyuncu.toplanan_kartlar.extend(oyuncular[4].kartlar)
					oyuncular[4].kartlar.clear()
					enusttekikart = ''
			elif atilan != enusttekikart:
				if atilan[0][-1] == 'J':
					ensonalan = sira
					oyuncu.toplanan_kartlar.extend(oyuncular[4].kartlar)
					oyuncular[4].kartlar.clear()
					enusttekikart = ''				
				else:
					enusttekikart = atilan
	if iskambil.destem:
		for oyuncu in oyuncular[:4]:
			oyuncu.kartlar = iskambil.dagit(4)

#print(ensonalan)
oyuncular[ensonalan].toplanan_kartlar.extend(oyuncular[4].kartlar)

eb = 0
ebk = 5

if len(oyuncular[0].toplanan_kartlar) >len(oyuncular[1].toplanan_kartlar):
	ebk = 0
	eb = len(oyuncular[0].toplanan_kartlar)
else:
	ebk = 1
	eb = len(oyuncular[1].toplanan_kartlar)

if len(oyuncular[ebk].toplanan_kartlar) <len(oyuncular[2].toplanan_kartlar):
	ebk = 2
	eb = len(oyuncular[2].toplanan_kartlar)

if len(oyuncular[ebk].toplanan_kartlar) <len(oyuncular[3].toplanan_kartlar):
	ebk = 3
	eb = len(oyuncular[3].toplanan_kartlar)

#print(eb,ebk,oyuncular[ebk].toplanan_kartlar)
oyuncular[ebk].puan += 3


for oyuncu in oyuncular:
	print(oyuncu.ad,oyuncu.toplanan_kartlar,oyuncu.pisti)
















