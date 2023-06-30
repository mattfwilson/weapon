import itertools
import random
from class_info import *

CHAR_CLASS = str()
CHAR_LEVEL = 1
INVENTORY = []
CLASSES = ['Barbarian', 'Sorcerer', 'Rogue', 'Necromancer', 'Druid']
RARITY = ['Common', 'Uncommon', 'Rare', 'Legendary', 'Unique']

class Item:
    id_iter = itertools.count(1)
    def __init__(self):
        self.id = next(Item.id_iter)

class Weapon(Item):
    def __init__(self, weapon, adj, level):
        super().__init__()
        self._level = level
        self._weap_lvl = random.choice(self._level, self._level + 1)
        self._weap_type = ', '.join(random.choices(weapon))
        self._weap_adj = ', '.join(random.choices(adj))
        self._drop = self._weap_adj + ' ' + self._weap_type
        INVENTORY.append(self._drop)

    def __repr__(self):
        return self._adj, self._weap_type

    def get_id(self):
        return self.id

    def get_item_level(self):
        return self._weap_lvl

if __name__ == "__main__":
    while True:
        roll_input = input('Roll item? ')
        if roll_input in 'y':
            rarity_roll = random.choices(RARITY, weights=[10, 7, 4, 2, 1])
            item = Weapon(sor_weap_type, sor_common_adj, CHAR_LEVEL)
            print(', '.join(rarity_roll))
        elif roll_input == 'inv':
            print(f'Inventory: {INVENTORY}')
        else:
            for item in INVENTORY:
                print(item)
            print(f'Exiting...')
            break


