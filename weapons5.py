# To-Dos

# Unit test for ensuring each item rolled has proper attrs and structure for appending to INV_DETAILS
# Is there a way to make drop adj/types a dict and have the value be an int that is counted without duplicates so that they values can be dynamically called for weights?

import itertools
import random
from attr_info import *

CHAR_CLASS = str()
CHAR_LEVEL = 1
INV = {}
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
        self._rarity = ''.join(random.choices(RARITY, weights=[5, 4, 3, 2, 1]))
        self._level = 5
        self._weap_adj = ''.join(random.choices(adj.get(self._rarity)))
        self._weap_type = ''.join(random.choices(weapon))
        self._drop = self._weap_adj + ' ' + self._weap_type
        self._buff_slots = 0
        self._buffs = {}

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
        base_roll = random.randint(6, 12)
        self._buffs[base_buff] = base_roll 

        for slots in range(self._buff_slots - 1):
            pub_buff = ''.join(random.choice(public_attrs.get(''.join(random.choices(RARITY, weights=[10, 7, 5, 3, 2])))))
            while pub_buff in self._buffs:
                pub_buff = ''.join(random.choice(public_attrs.get(''.join(random.choices(RARITY, weights=[10, 7, 5, 3, 2])))))

            perc_roll = round(random.uniform(perc_attr.get(self._rarity)[0], perc_attr.get(self._rarity)[1]), 1)
            self._buffs[pub_buff] = perc_roll

        assert self._buff_slots == len(self._buffs), f'{self._rarity} item, ({len(self._buffs)}) buffs, ({self._buff_slots}) slots'
        self._buffs['ID'] = self.id
        return self._buffs

    def add_to_inv(self):
        INV[self._drop] = self._buffs

    def show_drop(self):
        print('-' * 10 + ' [' + self._rarity + '] ' + self._drop + ' ' + '-' * 10)
        for attr in self._buffs:
            if isinstance(self._buffs[attr], int):
                print(f'- {attr}: +{self._buffs[attr]}')
            else:
                print(f'- {attr}: +{self._buffs[attr]}%')

    def show_details(self):
        print(f'\n- ID: {self.id}\n- Equipment: {self.type_equip}\n- Consumable: {self.type_consume}\n- Account Bound: {self.type_bound}\n- Buff slots: {self._buff_slots}\n')

    def __repr__(self):
        return f'[ID: {self.id} - {self._rarity} {self._weap_adj} {self._weap_type}]'

def show_inv(inventory):
    print('-' * 10 + ' INVENTORY ' + '-' * 10)
    for item in inventory:
        print(f'{list(inventory).index(item)} {item}')
    print(f'\n')

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
            show_inv(INV)
        else:
            print(f'Exiting...')
            break

