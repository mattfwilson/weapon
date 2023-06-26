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
        self.id = next(Common.id_iter)

class Common(Weapon):
    def __init__(self):
        super().__init__()
        INVENTORY.append(self)

    def __repr__(self):
        return f'Weapon {self.id}'

    def get_level(self, level):
        return f'Item level: {self.item_level}'

if __name__ == "__main__":
    CHAR_CLASS = 'Sorcerer'
    if CHAR_CLASS in CLASSES:
        print(f'{CHAR_CLASS} is a valid class! Rolling weapons...')
        w1 = Common()
        print(INVENTORY)
    else:
        print(f'{CHAR_CLASS} is not a valid class. Exiting...')
