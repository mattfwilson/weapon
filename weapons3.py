import itertools
import random

CHAR_CLASS = str()
CHAR_LEVEL = 1
INVENTORY = []
CLASSES = ['Barbarian', 'Sorcerer', 'Rogue', 'Necromancer', 'Druid']
RARITY = {'Legendary': 2.0, 'Rare': 17.5, 'Uncommon': 30.5, 'Common': 50.0}
SORCERER_ATTR = {'Strength', RARITY.get('Legendary'), 'Intelligence', RARITY.get('Common'), 'Dexerity', RARITY.get('Rare'), 'Willpower', RARITY.get('Common'), 'Vitality', RARITY.get('Uncommon')}

class Weapon:
    id_iter = itertools.count(1)
    def __init__(self):
        self.id = next(Weapon.id_iter)

class Common(Weapon):
    def __init__(self):
        super().__init__()
        self.item_level = self.id + 1
        INVENTORY.append(self)

    def __repr__(self):
        return f'Weapon {self.id}'

    def get_item_level(self):
        return self.item_level

if __name__ == "__main__":
    CHAR_CLASS = 'Sorcerer'
    if CHAR_CLASS in CLASSES:
        print(f'You are a {CHAR_CLASS}! Rolling weapon...')
        common1 = Common()
        print(f'Inventory: {INVENTORY}')
        print(f'{common1}, Item Level: {common1.get_item_level()}')
    else:
        print(f'{CHAR_CLASS} is not a valid class. Exiting...')
