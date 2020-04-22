from random import randint

CHARS = []
class Person:
    global CHARS
    def __init__(self, personTpl : tuple, Enemy : bool):
        global CHARS
        self.Dmg = personTpl[0]
        self.Hp = personTpl[1]
        self.Accuracy = personTpl[2]
        self.Crit = personTpl[3]
        self.Dodge = personTpl[4]
        self.Protection = personTpl[5]
        self.Speed = personTpl[6]
        self.Enemy = Enemy
        CHARS.append(self)

    @staticmethod
    def getobjbyname(name):
        for i in CHARS:
            if (i.Name == name):
                return i

    @staticmethod
    def getindbyname(name):
        for i in CHARS:
            if (i.Name == name):
                return CHARS.index(i)

    @staticmethod
    def namethem():
        global CHARS
        for self in CHARS:
            self.Name = CHARS.index(self)

    @staticmethod
    def view():
        global CHARS
        sentence = ''
        for i in CHARS:
            if (i.Enemy == False):
                sentence += str(i.Name) + ' '
        sentence += '\/ '
        for i in CHARS:
            if (i.Enemy == True):
                sentence += str(i.Name) + ' '
        print(sentence)

    def attack(self, other):
        if (self.Enemy != other.Enemy):
            dodgechance = randint(1, 100)

            for i in range(self.Dodge):
                if (i == dodgechance):
                    print(f'{str(CHARS.index(other))} уклоняется от атаки.\nЕго здоровье составляет {str(other.Hp)} HP.')
                    return

            crit = False
            critchance = randint(1, 100)

            for i in range(self.Crit):
                if (i == critchance):
                    crit = True

            other.Hp -= self.Dmg
            print(f'{str(self.Name)} атаковал {str(other.Name)}. У {str(other.Name)} осталось {str(other.Hp)} HP.')

            if (crit):
                other.Hp -= self.Dmg
                print(f'КРИТ! У {other.Name} теперь {other.Hp} HP')
            if (other.Hp <= 0):
                print(f'{str(other.Name)} погиб.')
                CHARS.remove(other)

                Person.view()

TYPE = (1, 2, 3, 100, 30, 6, 7)
for i in range(3):
    Person(TYPE, False)
for i in range(3):
    Person(TYPE, True)
Person.namethem()
Person.view()
CHARS[0].attack(CHARS[3])
while (True):
    exec(input())
