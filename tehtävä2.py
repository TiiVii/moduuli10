class Hissi():
    def __init__(self, alin, ylin):
        self.alin=alin
        self.ylin=ylin
        self.kerros = alin

    def siirry_kerrokseen(self, siirto):
        if siirto != self.kerros:
            while siirto > self.kerros:
                if self.kerros>=self.ylin:
                    return
                self.kerros_ylos()
            while siirto < self.kerros:
                if self.kerros<=self.alin:
                    return
                self.kerros_alas()

    def kerros_ylos(self):
       self.kerros += 1
       print(f'Olet kerroksessa {self.kerros}')
    def kerros_alas(self):
        self.kerros -= 1
        print(f'Olet kerroksessa {self.kerros}')



class Talo():
    def __init__(self, alin, ylin, hissi_maara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        self.hissi_maara = hissi_maara
        for hissi in range(hissi_maara):
            self.hissit.append(Hissi(self.alin, self.ylin))

    def aja_hissia(self, hissi_nro, kohdekerros):
        hissukka = self.hissit[hissi_nro]
        hissukka.siirry_kerrokseen(kohdekerros)

talo1= Talo(0,9,2)

talo1.aja_hissia(1,5)

