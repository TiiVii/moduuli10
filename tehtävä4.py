import random
from tabulate import tabulate


#auton luominen
class auto():
    def __init__(self, rekisteri, hnopeus, thnopeus, kmatka):
        self.rekisteri = rekisteri
        self.hnopeus = hnopeus
        self.thnopeus = thnopeus
        self.kmatka = kmatka

#auton tämän hetkisen nopeuden muuttaminen huomioiden huippunopeuden
    def kiihdyta(self, muutos):
        self.thnopeus += muutos
        if self.thnopeus>self.hnopeus:
            self.thnopeus=self.hnopeus
        if self.thnopeus<0:
            self.thnopeus=0

#auton kulkeman matkan määrä
    def kulje(self, tuntimaara):
        self.kmatka += (tuntimaara * self.thnopeus)

#kilpailut
class Kilpailu():
    def __init__(self, nimi, km, auton_muodostus):
        self.nimi = nimi
        self.km= km
        self.tunti=0
        self.autotalli = []
        self.auton_muodostus = auton_muodostus
        for jeejee in range(auton_muodostus):
            auton_muodostus = auto((f'ABC-{jeejee + 1}'), random.randint(100, 200), 0, 0)
            self.autotalli.append(auton_muodostus)

#kilpailu ohi kun auton kulkema matka on suurempi kuin kilpailun maximi määrä
    def kilpailu_ohi(self):
        self.ohion = False
        for auto in self.autotalli:
            if auto.kmatka>self.km:
                self.ohion=True
        return self.ohion

#yksi tunti kuluu ja kun se kuluu, arvotaan auton kiihdytysarvo
    def tunti_kuluu(self):
        self.tunti +=1
        for Kilpailu.auton_muodostus in self.autotalli:
            Kilpailu.auton_muodostus.kiihdyta(random.randint(-10,15))
            Kilpailu.auton_muodostus.kulje(1)

#tulostetaan arvot, mitä saatu 10 tunnin välein
    def tulosta_tilanne(self):
        yhteenveto = []
        for self.auton_muodostus in self.autotalli:
            yhteenveto.append((self.auton_muodostus.rekisteri, self.auton_muodostus.hnopeus, self.auton_muodostus.thnopeus,
                               self.auton_muodostus.kmatka, self.tunti))
        if self.tunti % 10 == 0 or self.kilpailu_ohi():
            print(tabulate(yhteenveto,
                       headers=['Rekisteri', 'Huippunopeus', 'Tämänhetkinen nopeus', 'Kuljettumatka', 'Kuluneet tunnit'],
                       tablefmt='double_grid'))


kilpailu1= Kilpailu("Suuri romuralli", 8000, 10)

while not kilpailu1.kilpailu_ohi():
    kilpailu1.tunti_kuluu()
    kilpailu1.tulosta_tilanne()

#tee autot paaohjelmassa t.aliisa
#looppaa tuntia niin pitkään, kunne km matka on saavutettu

#when race over print ja silleen jeejee
