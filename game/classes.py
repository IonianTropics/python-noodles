"""
8/19/2020

Character & item classes
"""
from typing import List


class Item:
    eqptslots: List[str]

    def __init__(self, slot=0, iseqpt=False, iscons=False, eqptslots=None):
        if eqptslots is None:
            self.eqptslots = ['none', 'mainhand', 'offhand', 'head', 'body', 'legs', 'feet', 'pack']
        self.slot = self.eqptslots[slot]
        self.iseqpt = iseqpt
        self.iscons = iscons


class Weapon(Item):

    def __init__(self, desc, typ):
        super().__init__(slot=1, iseqpt=True)
        self.desc = desc  # Temporarily strings, but will likely encode item modifiers later
        self.typ = typ
        self.name = str(self.desc) + str(self.typ)


class Head(Item):

    def __init__(self, desc, typ):
        super().__init__(slot=2, iseqpt=True)
        self.desc = desc  # Temporarily strings, but will likely encode item modifiers later
        self.typ = typ
        self.name = str(self.desc) + str(self.typ)


class Inv:

    def __init__(self, capacity, coin, invslots=None):
        if invslots is None:
            self.invslots = [''] * capacity
        self.eqpt = [''] * 8
        self.cap = capacity
        self.coin = coin


class Char(Inv):

    def __init__(self, name, hp, actions, capacity, coin):
        super().__init__(capacity, coin)
        self.name = name
        self.hp = hp
        self.actions = actions


p1 = Char('Yondu', 12, 0, 16, 140)


def giveitem(entity, item):
    try:
        inde = entity.invslots.index('')
    except ValueError:
        inde = None
    if inde is None:
        print("Inventory full")
    else:
        entity.invslots[inde] = item
    return 0


def takeitem(entity, item):
    try:
        inde = entity.invslots.index(item)
    except ValueError:
        inde = None
    if inde is None:
        print("Cannot find " + item.name)
    else:
        entity.invslots[inde] = ''
    return 0


def donitem(entity, item):
    if item in entity.invslots:
        if item.iseqpt:
            inde = entity.invslots.index(item)
            entity.invslots[inde] = ''
            entity.eqpt[item.slot] = item
        else:
            print('cannot equip ' + item.name)
    else:
        print(item.name + " not found")
    return 0


def doffitem(entity, item):
    if item in entity.eqpt:
        inde = entity.invslots.index(item)
        entity.invslots[inde] = item
        entity.eqpt[item.slot] = ''
    return 0


rusty_dagger = Weapon('nasty', 'knife')

giveitem(p1, rusty_dagger)


