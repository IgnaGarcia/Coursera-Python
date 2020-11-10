class Player(object):
    def __init__(self, name, rol, endurance, agility, armours):
        self.name = name
        self.rol = rol
        self.endurance = endurance
        self.agility = agility
        self.armours = armours

    def __repr__(self):
        return "{} {}: \n\tEndurance:\t{}\n\tAgility:\t{}\n\tArmours:{}".format(
            self.name, self.rol, self.endurance, self.agility, self.armours)

    def reducedDmg(self, DMG, armour):
        dmg = DMG * self.armours[armour].endurance / \
            (self.armours[armour].endurance + self.endurance)
        return round(dmg)

    def walkSpeed(self, armour):
        return 1.2*(((self.agility + self.armours[armour].agility) * 0.0043)+1.1)*2.2

    def runSpeed(self, armour):
        return 1.2*(((self.agility + self.armours[armour].agility) * 0.0043)+1.1)*3.5


class Rol(object):
    def __init__(self, name, bonus):
        self.name = name
        self.bonus = bonus

    def __repr__(self):
        return "[{} x{}]".format(self.name, self.bonus)


class Armour(object):
    def __init__(self, name, endurance, agility, absorcion):
        self.name = name
        self.endurance = endurance
        self.agility = agility
        self.absorcion = absorcion

    def __repr__(self):
        return "[{}({}%): {} - {}];\t".format(self.name, self.absorcion, self.agility, self.endurance)


# Instanciar Armaduras
bioReactive = Armour("BioReactive", 15, 20, 85)
reactiveXT = Armour("ER XT", 18, 15, 85)

# Instanciar Roles
Soldier = Rol("Soldier", 0.8)
Student = Rol("Student", 1.22)
Roler = Rol("RolPlayer", 1.3)
NonBonus = Rol("NonBonusPlayer", 1)

# Instanciar Personajes
NachUltra = Player("NachUltra", Roler, 100, 100, [bioReactive, reactiveXT])
print(NachUltra)
print(NachUltra.reducedDmg(1000, 2))


input()
