class Ristkylik():
    def __init__(self, l, k, s):
        self.laius = l
        self.korgus = k
        self.symbol = s
    def __str__(self):
        ruutu_read = []
        for rea_number in range(self.korgus):
            rida = self.symbol * self.laius
            ruutu_read.append(rida)

kujund1 = Ristkylik(10, 3, '*')
print('\n'.join(ruutu_read)
return ruutu_read

def __add__(self, teine_ristkylik):
    laius = self.laius + teine_ristkylik.laius
    korgus = self.korgus + teine_ristkylik.korgus
    symbol = teine_ristkylik.symbol
    return self.__init__(self, laius, korgus, symbol)