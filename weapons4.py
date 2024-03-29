# To-Dos

# Conditional for check on whether attr is int or float (percent)
# Unit test for ensuring each item rolled has proper attrs and structure for appending to INV_DETAILS
# Make dict of different lists for rarity of an attr roll, e.g. a legendary roll of attributes is weighted more towards legendary affix lists, where a magic roll is weighted more towards common/magic affix lists

import itertools
import random
from attr_info import *

CHAR_CLASS = str()
CHAR_LEVEL = 1
INV = []
INV_DETAILS = {}
RARITY = ['Common', 'Magic', 'Rare', 'Legendary', 'Unique']

class Item:
    id_iter = itertools.count(1)
    def __init__(self):
        self.id = next(Item.id_iter)
        self.type_equip = False
        self.type_consume = False
        self.type_bound = False

class Weapon(Item):
    def __init__(self, adj: dict, weapon: list):
        super().__init__()
        self.type_equip = True
        self._rarity = ''.join(random.choices(RARITY, weights=[1, 1, 1, 1, 1]))
        self._level = 5
        self._weap_adj = ''.join(random.choices(adj.get(self._rarity)))
        self._weap_type = ''.join(random.choices(weapon))
        self._drop = self._weap_adj + ' ' + self._weap_type
        self._buff_slots = 0
        self._buffs = []

    def roll_slots(self):
        assert isinstance(self._rarity, str), 'self._rarity is not a string'
        match self._rarity:
            case 'Unique':
                self._buff_slots = random.randint(5, 7)
                self.type_bound = True
            case 'Legendary':
                self._buff_slots = random.randint(4, 5)
                self.type_bound = True
            case 'Rare':
                self._buff_slots = 3
            case 'Magic':
                self._buff_slots = 2
            case 'Common':
                self._buff_slots = 1

    def roll_attrs(self, sor_attrs, public_attrs):
        base_buff = ''.join(random.choices(sor_attrs, weights=[10, 7, 3, 2, 1]))
        self._buffs.append(base_buff)

        for slots in range(self._buff_slots - 1):
            pub_buff = ''.join(random.choice(public_attrs.get(''.join(random.choices(RARITY, weights=[10, 7, 5, 3, 2])))))
            while pub_buff in self._buffs:
                pub_buff = ''.join(random.choice(public_attrs.get(''.join(random.choices(RARITY, weights=[10, 7, 5, 3, 2])))))
            self._buffs.append(pub_buff)

        assert self._buff_slots == len(self._buffs), f'{self._rarity} item, ({len(self._buffs)}) buffs, ({self._buff_slots}) slots'
        return self._buffs

    def add_to_inv(self):
        INV.append(self._drop)

    def show_drop(self):
        print(f'\n---------- [{self._rarity}] {self._drop} ----------')
        for att in self._buffs:
            print(f'- {att}')

    def show_details(self):
        print(f'\n- Equipment: {self.type_equip}\n- Consumable: {self.type_consume}\n- Account Bound: {self.type_bound}\n- Buff slots: {self._buff_slots}\n')

    def __repr__(self):
        return f'[ID: {self.id} - {self._rarity} {self._weap_adj} {self._weap_type}]'

if __name__ == "__main__":
    while True:
        roll_input = input('What do you want to do? ')
        if roll_input == 'roll':
            item = Weapon(sor_adj, sor_weap)
            item.roll_slots()
            item.roll_attrs(sor_attrs, public_attrs)
            item.add_to_inv()
            item.show_drop()
            item.show_details()
        elif roll_input == 'inv':
            print(f'Inventory: {INV}')
        else:
            print(f'Exiting...')
            break

