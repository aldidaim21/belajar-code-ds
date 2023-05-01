class Hero:
    # class variabel
    jumlahhero = 0

    def __init__(self, name, health, power, armor):
     # intance variabel
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        Hero.jumlahhero += 1

    # method void tanpa return
    def asep(self):
        print('namaku adalah', self.name)

    # method argumen
    def helathUp(self, up):
        self.health += up

    # method return
    def gethealth(self):
        return self.health


hero1 = Hero('sniper', 10, 10, 10)
hero1.asep()
hero1.helathUp(10)  # akan meneaikan health menjadi 20
print(hero1.gethealth())
