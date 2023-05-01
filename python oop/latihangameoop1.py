class Hero:
    def __init__(self, nama, darah, serang, kekuatan):
        self.nama = nama
        self.darah = darah
        self.serang = serang
        self.kekuatan = kekuatan

    def nyerang(self, Hero):
        print(self.nama + ' menyerang ' + Hero.nama)
        Hero.diserang(self, self.serang)

    def diserang(self, Hero, attackpower_lawan):
        print(self.nama + ' diserang ' + Hero.nama)
        attack_diterima = attackpower_lawan / self.kekuatan

        # membuat informasi damage
        self.darah -= attack_diterima
        print("seranga terasa : " + str(attack_diterima))
        print('darah ' + self.nama + ' tersisa ' + str(self.darah))


sniper = Hero('sniper', 100, 200, 20)
balmond = Hero('balmomd', 100, 100, 50)
sniper.nyerang(balmond)

print("/n")

sniper.nyerang(balmond)
