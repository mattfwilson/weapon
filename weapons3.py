import itertools
import random
from class_info import *

CHAR_CLASS = str()
CHAR_LEVEL = 1
INVENTORY = []
RARITY = ['Common', 'Magic', 'Rare', 'Legendary', 'Unique']

class Item:
    id_iter = itertools.count(1)
    def __init__(self):
        self.id = next(Item.id_iter)
        self.type_equipment = True
        self.type_consumable = False
        self.account_bound = False

class Weapon(Item):
    def __init__(self, adj: dict, weapon: list):
        super().__init__()
        self._rarity = ''.join(random.choices(RARITY, weights=[10, 7, 4, 2, 1]))
        self._level = 5
        self._weap_adj = ''.join(random.choices(adj.get(self._rarity)))
        self._weap_type = ''.join(random.choices(weapon))
        self._drop = self._weap_adj + ' ' + self._weap_type
        self._buff_slots = 0
        self._buffs = []

    def roll_slots(self):
        if self._rarity == 'Unique':
            self._buff_slots = random.randint(5, 6)
            self.account_bound = True
        elif self._rarity == 'Legendary':
            self._buff_slots = random.randint(4, 5)
            self.account_bound = True
        elif self._rarity == 'Rare':
            self._buff_slots = 3
        elif self._rarity == 'Magic':
            self._buff_slots = 2
        else:
            self._buff_slots = 1
        return self._buff_slots

    def roll_attrs(self, sor_attrs, public_attrs):
        print(self._rarity)
        print(f'Buff slots before loop: {self._buff_slots}')
        self._buffs.append(''.join(random.choices(sor_attrs, weights=[10, 7, 3, 2, 1])))
        print(f'Buffs before loop: {self._buffs}')
        self._buff_slots -= 1
        if self._buff_slots > 0:
            for slot in range(self._buff_slots):
                self._buffs.append(''.join(random.sample(public_attrs.get(self._rarity), 1)))
                self._buff_slots -= 1
        print(f'Buffs after loop: {self._buffs}')
        print(f'Buff slots after loop: {self._buff_slots}')
        return self._buffs
    def add_to_inv(self):
        INVENTORY.append(self._drop)

    def __repr__(self):
        return self._adj, self._weap_type

    def get_id(self):
        return self.id

    def show_drop(self):
        print(f'[{self._rarity}] {self._drop}')
        for att in self._buffs:
            print(att)

    def show_details(self):
        print(f'Equipment: {self.type_equipment}\nConsumable: {self.type_consumable}\nQuest item: {self.account_bound}\nBuff slots: {self._buff_slots}')

if __name__ == "__main__":
    while True:
        roll_input = input('What do you want to do? ')
        if roll_input == 'roll':
            item = Weapon(sor_adj, sor_weap)
            item.roll_slots()
            item.roll_attrs(sor_attrs, public_attrs)
            item.add_to_inv()
        elif roll_input == 'inv':
            print(f'Inventory: {INVENTORY}')
        else:
            print(f'Exiting...')
            break

