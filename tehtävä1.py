class Hissi():
    def __init__(self, alin, ylin, kerros):
        self.alin=0
        self.ylin=9
        self.kerros = kerros

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


h= Hissi(0,0,0)

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(0)