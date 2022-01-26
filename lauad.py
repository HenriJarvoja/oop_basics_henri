class Laud():
    def __init__(self, p, l, k):
        self.pikkus = p
        self.laius = l
        self.korgus = k
class Koogilaud(Laud):
    def kohad(self, ka):
        self.kohtade_arv = ka
class Kirjutuslaud(Laud):
    def pindala(self:
    self.pikkus = self.laius
class Arvutilaud(Kirjutuslaud):
    def pindala(self, arvuti):
        return self.pikkus * self.laius - arvuti
laud1 = Koogilaud(2, 2, 0.7)
laud2 = Koogilaud(1, 1.5, 0.75)
laud3 = Kirjalaud()

