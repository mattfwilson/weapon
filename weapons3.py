import itertools
import random

CHAR_CLASS = str()
CHAR_LEVEL = 23
INVENTORY = []
CLASSES = ['Barbarian', 'Sorcerer', 'Rogue', 'Necromancer', 'Druid']
RARITY = {'Legendary': 2.0, 'Rare': 17.5, 'Uncommon': 30.5, 'Common': 50.0}
SORCERER_ATTR = {'Strength', RARITY.get('Legendary'), 'Intelligence', RARITY.get('Common'), 'Dexerity', RARITY.get('Rare'), 'Willpower', RARITY.get('Common'), 'Vitality', RARITY.get('Uncommon')}

class CommonWeapon:
    id_iter = itertools.count(0)
    gen_attr_range = {'is_class': [6.0, 16.0], 'not_class': [4.0, 12.0]}

    def __init__(self, level):
        self.id = next(CommonWeapon.id_iter)
        self.level = level
        INVENTORY.append(self)

    def __repr__(self):
        return f'Weapon {self.id}'

    def get_level(self, level):
        return f'Item level: {self.level}'

print(__name__, type(__name__))

if __name__ == "__main__":
    while True:
        CHAR_CLASS = input('What is your class? ')
        if CHAR_CLASS in CLASSES:
            print(f'{CHAR_CLASS} is a valid class! Rolling weapons...')
            w1 = CommonWeapon(CHAR_LEVEL)
            print(f'{w1} was created! {w1.get_level(CHAR_LEVEL)}')
            w2 = CommonWeapon(CHAR_LEVEL)
            print(f'{w2} was created!')
            w3 = CommonWeapon(CHAR_LEVEL)
            print(f'{w3} was created!')
            print(INVENTORY)
        else:
            print(f'{CHAR_CLASS} is not a valid class. Breaking loop')
            break
