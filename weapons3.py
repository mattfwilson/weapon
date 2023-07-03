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
    def check_rarity(self):
        if self._rarity == 'Unique':
            self._rarity = self._rarity.upper()
            self._buff_slots = random.randint(4, 6)
        elif self._rarity == 'Legendary':
            self._rarity = self._rarity.upper()
            self._buff_slots = random.randint(3, 5)
        elif self._rarity == 'Rare':
            self._buff_slots = 3
        elif self._rarity == 'Magic':
            self._buff_slots = 2
        else:
            self._buff_slots = 1
        roll_attrs(self._buff_slots)

    def roll_attrs(self, slots):
        self._buffs.append(random.choices(sor_attrs.get(self._rarity, weights=[10, 7, 3, 2, 1])))
        slots -= 1
        if slots > 0:
            for slot in range(slots):
                self._buffs.append(random.choices(public_attrs.get(self._rarity, weights[5, 4, 3, 2, 1])))
        return self._buffs

    def __init__(self, rarity: str, adj: dict, weapon: list):
        super().__init__()
        self._rarity = rarity
        self._level = 5
        self._weap_adj = ''.join(random.choices(adj.get(self._rarity)))
        self._weap_type = ''.join(random.choices(weapon))
        self._drop = self._weap_adj + ' ' + self._weap_type
        self._buff_slots = check_rarity()
        self._buffs = []
        roll_attrs()
        INVENTORY.append(self._drop)

    def __repr__(self):
        return self._adj, self._weap_type

    def get_id(self):
        return self.id

    def show_drop(self):
        print(f'[{self._rarity}] {self._drop}')

    def show_details(self):
        print(f'Equipment: {self.type_equipment}\nConsumable: {self.type_consumable}\nQuest item: {self.account_bound}\nBuff slots: {self._buff_slots}')

def show_full_drop(item):
    item.show_drop()
    item.show_details()

if __name__ == "__main__":
    while True:
        roll_input = input('What do you want to do? ')
        if roll_input in 'roll':
            rarity_roll = ''.join(random.choices(RARITY, weights=[10, 7, 4, 2, 1]))
            item = Weapon(rarity_roll, sor_adj, sor_weap)
            show_full_drop(item)
        elif roll_input == 'inv':
            print(f'Inventory: {INVENTORY}')
        else:
            print(f'Exiting...')
            break

