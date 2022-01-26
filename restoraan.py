class Restoraan():
    restoraani_nimi = 'mingi nimi'
    soogi_tyyp = 'mingi sook'

    def kirjelda_restoraan(self):
        print('Restoraan ' + str(self.restoraani_nimi) + 'pakub ' + str(self.soogi_tyyp))

    def ava_restoraan(self):
        print('Restoraan on avatud')

resto1 = Restoraan()
resto1.restoraani_nimi = 'Krõbekana '
resto1.soogi_tyyp = 'linnuliha'
resto1.kirjelda_restoraan()
resto1.ava_restoraan()

resto2 = Restoraan()
resto2.restoraani_nimi = 'Minu resto '
resto2.soogi_tyyp = 'loomaliha'
resto2.kirjelda_restoraan()
resto2.ava_restoraan()

resto3 = Restoraan()
resto3.restoraani_nimi = 'Naabri Hiina restoran '
resto3.soogi_tyyp = 'kassiliha'
resto3.kirjelda_restoraan()
resto3.ava_restoraan()
