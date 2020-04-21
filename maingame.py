from random import randint

CHARS = []
class Person:
    global CHARS
    def __init__(self, personTpl : tuple, enemy : bool):
        self.Dmg = personTpl[0]
        self.Hp = personTpl[1]
        self.Accuracy = personTpl[2]
        self.Crit = personTpl[3]
        self.Dodge = personTpl[4]
        self.Protection = personTpl[5]
        self.Speed = personTpl[6]
        self.enemy = enemy
        CHARS.append(self)
    @staticmethod
    def view():
        global CHARS
        sentence = ''
        for i in range(len(CHARS)):
            if (CHARS[i].enemy == False):
                sentence += str(i) + ' '
        sentence += '\/ '
        for i in range(len(CHARS)):
            if (CHARS[i].enemy == True):
                sentence += str(i) + ' '
        print(sentence)
    def attack(self, other):
        if (self.enemy != other.enemy):
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
            iself = CHARS.index(self)
            iother = CHARS.index(other)
            print(f'{str(iself)} атаковал {str(iother)}. У {str(iother)} осталось {str(other.Hp)} HP.')
            if (crit):
                other.Hp -= self.Dmg
                print(f'КРИТ! У {iother} теперь {other.Hp} HP')
            if (other.Hp <= 0):
                print(f'{str(iother)} погиб.')

TYPE = (1, 2, 3, 100, 50, 6, 7)
for i in range(3):
    Person(TYPE, False)
for i in range(3):
    Person(TYPE, True)
Person.view()
CHARS[0].attack(CHARS[3])
while (True):
    exec(input())
