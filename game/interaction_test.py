"""
8\19\2020

Simple Combat
"""

# Imports

import sys
import random
import time


# Initialization

class Char:
    name: str
    hp: int
    actions: int
    mainhand: str

    def __init__(self, name, hp, mainhand, actions=0):
        """

        :type name: str
        :type hp: int
        :type actions: int
        :type mainhand: string
        """

        self.name = name
        self.hp = hp
        self.actions = actions
        self.mainhand = mainhand


player = Char(name="you", hp=12, mainhand='knife')
troll = Char('Troll', 12, mainhand='sword')

# StartX

loop = input("for latest version type '1' for stable/old versions type '2'\n")

# sys.exit()  # Uncomment to disable game
if loop == '2':
    # old loop:
    while True:  # Whole interaction in here
        if p1.hp > 0:
            stimuli = troll.name + ' raises his ' + troll.mainhand
            print('\n' + stimuli)
            time.sleep(0.8)
            p1.actions += 1
            while p1.actions > 0:
                action = input('\n').capitalize()
                time.sleep(0.8)
                if action == 'Attack troll with ' + p1.mainhand:
                    dmg = random.randint(1, 4) + random.randint(1, 4)
                    troll.hp -= dmg
                    print('\n' + troll.name + ' takes ' + str(dmg) + ' damage')
                    p1.actions -= 1
                elif action == p1.name:
                    sys.stdout.write('\n{0}'.format('Name:     ' + "'" + p1.name.capitalize() + "'") +
                                     '\n{0}'.format('HP:       ' + str(p1.hp)) +
                                     '\n{0}'.format('Mainhand: ' + p1.mainhand) +
                                     '\n{0}'.format('Offhand:  ' + 'none') +
                                     '\n{0}'.format('Head:     ' + 'none') +
                                     '\n{0}'.format('Chest:    ' + 'none') +
                                     '\n{0}'.format('Legs:     ' + 'none') +
                                     '\n{0}'.format('Feet:     ' + 'none') +
                                     '\n' * 2)
                else:
                    continue
        else:
            for i in range(10):
                time.sleep(0.4)
                txt = list('GAME OVER')
                sys.stdout.write('\r{0}'.format(''.join(txt[0:i])))
            time.sleep(1)
            sys.exit()
        time.sleep(0.8)
        if troll.hp > 0:
            troll.actions += 1
            while troll.actions > 0:
                troll.actions -= 1
                print('\n' + troll.name + ' swings his ' + troll.mainhand)
                dmg = random.randint(1, 4) + random.randint(1, 4)
                p1.hp -= dmg
                time.sleep(0.6)
                print('You take ' + str(dmg) + ' damage')
        else:
            print(troll.name + ' collapses to the ground')
            input('Test will end')
            sys.exit()
        time.sleep(0.8)
        continue
elif loop == '1':
    # new loop
    while True:
        time.sleep(0.6)  # Turn Description
        if player.hp > 0 and troll.hp > 0:
            desc = troll.name.capitalize() + "raises their" + troll.mainhand
        elif player.hp > 0 >= troll.hp:
            desc = troll.name.capitalize() + "lies dead"
        elif player.hp <= 0 < troll.hp:
            print("GAME OVER")
            time.sleep(5)
            sys.exit()
        else:
            desc = -1
            print("Error, desc is unexpected value")
        print("\n" + desc + "\n")
        time.sleep(0.6)  # Player Turn
        if player.hp > 0:
            player.actions = 1
            while player.actions > 0:
                print("\nYour turn:\n")
                choice = input()
                if choice == ("attack " + troll.name + " with " + player.mainhand):
                    troll.hp -= random.randint(4, 6)
                    player.actions -= 1
                elif choice == "inventory":
                    sys.stdout.write('\n{0}'.format('HP:       ' + str(player.hp)) +
                                     '\n{0}'.format('Mainhand: ' + player.mainhand) +
                                     '\n{0}'.format('Offhand:  ' + 'none') +
                                     '\n{0}'.format('Head:     ' + 'none') +
                                     '\n{0}'.format('Chest:    ' + 'none') +
                                     '\n{0}'.format('Legs:     ' + 'none') +
                                     '\n{0}'.format('Feet:     ' + 'none') +
                                     '\n' * 2)
                else:
                    print("No option '" + choice + "'")
                continue
        # Opponents Turn(s)
            player.hp -= random.randint(4, 6)
        continue
