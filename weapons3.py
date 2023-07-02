import itertools
import random
from class_info import *

CHAR_CLASS = str()
CHAR_LEVEL = 1
INVENTORY = []
CLASSES = ['Barbarian', 'Sorcerer', 'Rogue', 'Necromancer', 'Druid']
RARITY = ['Common', 'Magic', 'Rare', 'Legendary', 'Unique']

class Item:
    id_iter = itertools.count(1)
    def __init__(self):
        self.id = next(Item.id_iter)

class Weapon(Item):
    def __init__(self, rarity: str, adj: dict, weapon: list):
        super().__init__()
        self._rarity = rarity
        print(self._rarity)
        self._level = 5
        self._weap_adj = ''.join(random.choices(adj.get(self._rarity)))
        self._weap_type = ''.join(random.choices(weapon))
        self._drop = self._weap_adj + ' ' + self._weap_type
        print(self._drop)
        INVENTORY.append(self._drop)

    def __repr__(self):
        return self._adj, self._weap_type

    def get_id(self):
        return self.id

if __name__ == "__main__":
    while True:
        roll_input = input('Roll item? ')
        if roll_input in 'y':
            rarity_roll = ''.join(random.choices(RARITY, weights=[10, 7, 4, 2, 1]))
            item = Weapon(rarity_roll, sor_adj, sor_weap)
        elif roll_input == 'inv':
            print(f'Inventory: {INVENTORY}')
        else:
            print(f'Exiting...')
            break

