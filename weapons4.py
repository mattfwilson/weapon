# To-Dos

# Conditional for check on whether attr is int or float (percent)
# Unit test for ensuring each item rolled has proper attrs and structure for appending to INV_DETAILS
# Bug: buff slots not rolling for maximum amount of buff slots created
# Make assert for checking if buff slots match buffs created /

import itertools
import random
from class_info import *

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
        self._rarity = ''.join(random.choices(RARITY, weights=[10, 7, 4, 8, 8]))
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
                self._buff_slots = 6
                self.type_bound = True
            case 'Legendary':
                self._buff_slots = 5
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
        for slots in range(self._buff_slots):
            pub_buff = ''.join(random.choice(public_attrs.get(''.join(random.choices(RARITY, weights=[10, 7, 5, 3, 2])))))
            print(pub_buff)
            if pub_buff not in self._buffs:
                self._buffs.append(pub_buff)
            else:
                pub_buff = ''.join(random.choice(public_attrs.get(''.join(random.choices(RARITY, weights=[10, 7, 5, 3, 2])))))
        assert self._buff_slots == len(self._buffs), f'{self._rarity} item, ({len(self._buffs)}) buffs, ({self._buff_slots}) slots'
        return self._buffs

    def add_to_inv(self):
        INV.append(self._drop)

    def show_drop(self):
        print(f'\n---------- [{self._rarity}] {self._drop} ----------')
        for att in self._buffs:
            print(f'- {att}')

    def show_details(self):
        print(f'\nEquipment: {self.type_equip}\nConsumable: {self.type_consume}\nAccount Bound: {self.type_bound}\nBuff slots: {self._buff_slots}\n')

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

