class Kasutaja():
    eesnimi = ''
    perenimi = ''

    def kirjelda_kasutaja(self):
        print ("eesnimi: " + str(self.eesnimi)
        print ("perenimi: " + str(self.perenimi))

    def tervita_kasutajat(self):
        print("Tere, " + str(self.eesnimi) + str(self.perenimi))


kasutaja1 = Kasutaja()
kasutaja1.eesnimi = 'Henri'
kasutaja1.perenimi = 'Järvoja'

kasutaja1.kirjelda_kasutaja()
kasutaja1.tervita_kasutajat()

kasutaja2 = Kasutaja()
kasutaja2.eesnimi = 'Kärbes'
kasutaja2.perenimi = 'Jaak'

kasutaja2.kirjelda_kasutaja()
kasutaja2.tervita_kasutajat()

kasutaja3 = Kasutaja()
kasutaja3.eesnimi = 'Mati'
kasutaja3.perenimi = 'Maasikas'

kasutaja3.kirjelda_kasutaja()
kasutaja3.tervita_kasutajat()