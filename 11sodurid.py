class Inimene():
    jk = 0

def __init__(self):
    self.id = Inimene.jk + 1
    Inimene.jk += 1
def info(self):
    print("")

armee_1 = []
armee_2 = []

for kord in range(20):
    millisesse_armeesse = randint(1, 2)
    sodur = Sodur(millisesse_armeesse)
    if(millisesse_armeesse == 1):
        armee_1.append(sodur)
        if(millisesse_armeesse == 2):
            armee_2.append(sodur)

print('Armee 1')
for sodur in armee_1:
    sodur.info()
    print('-------------')
    print('Armee 2')
for sodur in armee_2:
    sodur.info()