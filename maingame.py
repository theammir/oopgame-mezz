from random import randint, choice

class Item:
    def __init__(self, charcsTpl):
        self.Type = charcsTpl[0]
        self.Buff = charcsTpl[1]
        self.Debuff = charcsTpl[2]
        self.Compatibility = charcsTpl[3]
        self.isEqiupped = False
        self.Owner = None

CHARS = []
MOVE  = {}
class Person:
    global CHARS
    def __init__(self, charcsTpl : tuple, Enemy : bool):
        global CHARS
        self.Dmg = charcsTpl[0]
        self.Hp = charcsTpl[1]
        self.MaxHP = charcsTpl[1]
        self.Accuracy = charcsTpl[2]
        self.Crit = charcsTpl[3]
        self.Dodge = charcsTpl[4]
        self.Protection = charcsTpl[5]
        self.Speed = charcsTpl[6]
        self.Enemy = Enemy
        CHARS.append(self)

    @staticmethod
    def getobjbyname(name):
        global CHARS
        for i in CHARS:
            if (i.Name == name):
                return i

    @staticmethod
    def namethem():
        global CHARS
        for self in CHARS:
            self.Name = CHARS.index(self)

    @staticmethod
    def view():
        global CHARS
        print('')
        sentence = ''
        for i in CHARS:
            if (i.Enemy == False):
                sentence += str(i.Name) + ' '
        sentence += '\/ '
        for i in CHARS:
            if (i.Enemy == True):
                sentence += str(i.Name) + ' '
        print(sentence)
        print('')

    @staticmethod
    def setmove():
        global CHARS
        global MOVE
        MOVE = {}
        temp = []
        for i in CHARS:
            temp.append(i)
        for i in range(1, len(CHARS) + 1):
            j = choice(temp)
            MOVE[i] = j
            temp.remove(j)


    def equip(self, item : Item):
        if (self.Enemy == False):
            if (item.isEqiupped != True):
                CharcsDict = {'HP' : self.MaxHP, 'DMG' : self.Dmg, 'DDG' : self.Dodge}
                CondList = ['<', '>']
                buffprr = item.Buff[item.Buff.index(' ') + 1:]
                def buff(self, item, prm, CharcsDict = CharcsDict, buffprr = buffprr):
                    if (prm == '+'):
                        print('')

                        print(f'{str(self.Name)} получил бафф {buffprr} от экипировки.')
                        buffval = int(item.Buff[:item.Buff.index(' ')])
                        print(f'Старый параметр: {str(CharcsDict[buffprr])} {buffprr}.')
                        CharcsDict[buffprr] += buffval
                        print(f'Новый параметр: {str(CharcsDict[buffprr])} {buffprr}.')

                        print('')
                    elif (prm == '-'):
                        buffprr = item.Debuff[item.Debuff.index(' ') + 1:]
                        print(f'{str(self.Name)} подвергся негативному воздействию на {buffprr}.')
                        buffval = int(item.Debuff[:item.Debuff.index(' ')])
                        print(f'Старый параметр: {str(CharcsDict[buffprr])} {buffprr}.')
                        CharcsDict[buffprr] -= buffval
                        print(f'Новый параметр: {str(CharcsDict[buffprr])} {buffprr}.')

                        print('')

                if (item.Compatibility[0] == CondList[0]):
                    # if (self.Hp < compatible (fe <10))
                    if (CharcsDict[item.Compatibility[item.Compatibility.index(' ') + 1:]] < int(item.Compatibility[1:item.Compatibility.index(' ')])):
                        buff(self, item, '+')
                        if (item.Debuff):
                            buff(self, item, '-')
                        item.isEqiupped = True
                        item.Owner = self
                    else:
                        print(f'Похоже, {str(self.Name)} не совместим с данным предметом.')
                elif (item.Compatibility[0] == CondList[1]):
                    if (CharcsDict[item.Compatibility[item.Compatibility.index(' ') + 1:]] > int(item.Compatibility[1:item.Compatibility.index(' ')])):
                        buff(self, item, '+')
                        if (item.Debuff):
                            buff(self, item, '-')
                        item.isEqiupped = True
                        item.Owner = self
                else:
                    print('[!] Недопустимый знак сравнения в условии совместмости предмета.')
            else:
                print(f'Предмет уже экипирован на {str(item.Owner.Name)}.')
        else:
            print('Вы выбрали недопустимую цель для экипировки.')

    def attack(self, other):
        if (self.Enemy != other.Enemy):
            print(f'{str(self.Name)} атаковал {str(other.Name)}. ')
            misschance = randint(1, 100)
            for i in range(100 - self.Accuracy):
                if (i == misschance):
                    print(f'{str(self.Name)} промахивается!\nЗдоровье {str(other.Name)} составляет {str(other.Hp)}/{str(other.MaxHP)} HP.')
                    return

            dodgechance = randint(1, 100)
            for i in range(self.Dodge):
                if (i == dodgechance):
                    print(f'{str(other.Name)} уклоняется от атаки.\nЕго здоровье составляет {str(other.Hp)}/{str(other.MaxHP)} HP.')
                    Person.view()
                    return

            crit = False
            critchance = randint(1, 100)
            for i in range(self.Crit):
                if (i == critchance):
                    crit = True

            other.Hp -= self.Dmg
            print(f'У {str(other.Name)} осталось {str(other.Hp)}/{str(other.MaxHP)} HP.')

            if (crit):
                other.Hp -= self.Dmg
                print(f'КРИТ! У {other.Name} теперь {str(other.Hp)}/{str(other.MaxHP)} HP')
            if (other.Hp <= 0):
                print(f'{str(other.Name)} погиб.')
                CHARS.remove(other)
            print('')
            input()

            Person.view()

    @staticmethod
    def round(CHARS = CHARS):
        global MOVE
        Person.setmove()
        for i in range(1, len(MOVE) + 1):
            i = MOVE[i]
            if (i in CHARS):
                print(f'{str(i.Name)} атакует!')
                if (i.Enemy == False):
                    attacked = int(input('Кого вы хотите атаковать?: '))
                    if (gobn(attacked)):
                        i.attack(gobn(attacked))
                    else:
                        print('Не существует такого персонажа, которого вы хотите атаковать.')
                elif (i.Enemy == True):
                    attacked = None
                    enemy = None
                    while (enemy != False):
                        attacked = choice(CHARS)
                        enemy = attacked.Enemy
                    i.attack(attacked)
                if (won()):
                    return

def gobn(n):
    return Person.getobjbyname(n)

def won():
    global CHARS
    temp = []
    for i in CHARS:
        temp.append(i.Enemy)
    temp = set(temp)
    if (len(temp) == 1):
        return True
    else:
        return False


print('Для продолжения после результатов атаки жмите Enter.')
TYPE = (5, 11, 85, 50, 30, 6, 7)
item = Item(('chestplate', '1 HP', '10 DDG', '>1 HP'))
for i in range(3):
    Person(TYPE, False)
for i in range(3):
    Person(TYPE, True)
Person.namethem()
Person.view()
gobn(1).equip(item)
while not (won()):
    Person.round()
print('GAME OVER')
