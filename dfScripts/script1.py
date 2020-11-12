class Player(object):
    def __init__(self, name, rol, endurance, agility, armours, gm, xpboost):
        self.name = name
        self.rol = rol
        self.endurance = endurance
        self.agility = agility
        self.armours = armours
        self.gm = gm
        self.xpBoost = xpboost  # Event, Drugs, Implants, 10% verifiqued account

    def __repr__(self):
        return "{} \n\t{}: \n\tEndurance:\t{}\n\tAgility:\t{}\n\tArmours:{}".format(
            self.name, self.rol, self.endurance, self.agility, self.armours)

    def expGain(self, zombie, DMG):
        return zombie.density * DMG * self.rol.bonus * \
            1.5 * self.gm * (1 + self.xpBoost)

    def reducedDmg(self, DMG, armour):
        dmg = DMG * self.armours[armour].endurance / \
            (self.armours[armour].endurance + self.endurance)
        return round(dmg)

    def takeDmg(self, DMG, armour):
        absorved = DMG * self.armours[armour].absorcion / 100
        mitigated = self.reducedDmg((DMG - absorved), armour)
        taked = DMG - (absorved + mitigated)
        return "\n\tTotal: {}\n\tAbsorvido: {}\n\tMitigado: {}\n\tRestante: {}".format(DMG, absorved, mitigated, taked)

    def walkSpeed(self, armour):
        speed = 1.2 * \
            (((self.agility + self.armours[armour].agility) * 0.0043)+1.1)*2.2
        return speed

    def runSpeed(self, armour):
        speed = 1.2 * \
            (((self.agility + self.armours[armour].agility) * 0.0043)+1.1)*3.5
        return speed


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
        return " [{}({}%): {} - {}] ".format(self.name, self.absorcion, self.agility, self.endurance)


class Zombie(object):
    def __init__(self, health, name, attack, altAttack, speed, density):
        self.name = name
        self.health = health
        self.attack = attack
        self.altAttack = altAttack
        self.speed = speed
        self.density = density


# Instanciar Armaduras
bioReactive = Armour("BioReactive", 15, 20, 85)
reactiveXT = Armour("ER XT", 18, 15, 85)
gc = Armour("GV", 24, 24, 85)

# Instanciar Roles
Soldier = Rol("Soldier", 0.8)
Student = Rol("Student", 1.22)
Roler = Rol("RolPlayer", 1.3)
NonBonus = Rol("NonBonusPlayer", 1)

# Instanciar Personajes
NachUltra = Player("NachUltra", Roler, 100, 100, [
                   bioReactive, reactiveXT, gc], 1, 0.1)

# Instanciar Zombies
hellHound = Zombie("Hell Hound", 500, 250, 0, 11, 1.875)
blackTendril = Zombie("Black Tendril", 300, 220, 0, 9, 1.875)
blackBone = Zombie("Black Bone", 600, 180, 200, 9, 1.875)

siren = Zombie("Siren", 70, 0, 0, 1.6, 2.143)
tendril = Zombie("Tendril", 235, 70, 0, 7, 1.277)
sprider = Zombie("Spider", 300, 40, 0, 7, 1.125)
bloat = Zombie("Bloat", 200, 40, 40, 4.5, 1.5)
brute = Zombie("Brute", 400, 30, 40, 4.5, 1.219)
leaper = Zombie("Leaper", 400, 9999, 0, 4.5, 1.219)

blackRumbler = Zombie("Black Rumbler", 250, 70, 0, 4.2, 1.14)
blackIrrRumbler = Zombie("Irradiated Black Rumbler", 250, 50, 60, 4.2, 1.14)
blackLongArm = Zombie("Black Long Arm", 200, 55, 0, 5.7, 1.313)
blackIrrLongArm = Zombie("Irradiated Black Long Arm", 200, 55, 110, 5.7, 1.313)
fleshHound = Zombie("Flesh Hound", 200, 100, 0, 11, 1.5)
# Pruebas
print(NachUltra)
print("\n")

print(NachUltra.reducedDmg(100, 0))
print(NachUltra.walkSpeed(0))
print(NachUltra.runSpeed(0))
print("\n")

print(NachUltra.reducedDmg(100, 1))
print(NachUltra.walkSpeed(1))
print(NachUltra.runSpeed(1))
print("\n")

print(NachUltra.reducedDmg(100, 2))
print(NachUltra.walkSpeed(2))
print(NachUltra.runSpeed(2))
print("\n")

print(NachUltra.takeDmg(700, 0))
print(NachUltra.takeDmg(700, 1))
print(NachUltra.takeDmg(700, 2))
print("\n")

print(NachUltra.expGain(hellHound, 120))
print(NachUltra.expGain(tendril, 120))
print(NachUltra.expGain(blackLongArm, 120))

input()
