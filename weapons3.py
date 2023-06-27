import itertools
import random
from class_info import *

CHAR_CLASS = str()
CHAR_LEVEL = 1
INVENTORY = []
CLASSES = ['Barbarian', 'Sorcerer', 'Rogue', 'Necromancer', 'Druid']
RARITY = {'Legendary': 3, 'Rare': 17, 'Uncommon': 30, 'Weapon': 50}

class Item:
    id_iter = itertools.count(1)
    def __init__(self):
        self.id = next(Item.id_iter)

class Weapon(Item):
    def __init__(self, weapon, adj):
        super().__init__()
        self._weap_lvl = self.id + 1
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
        roll_item = input('Roll item? ')
        if roll_item in 'y':
            print(f'Rolling weapon...')
            item = Weapon(sor_weap_type, sor_common_adj)
            print(f'Inventory: {INVENTORY}')
        else:
            for item in INVENTORY:
                print(item)
            print(f'Exiting...')
            break
