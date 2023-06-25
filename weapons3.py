import itertools
import random

CHAR_CLASS = str()
CHAR_LEVEL = 1
CLASSES = ['Barbarian', 'Sorcerer', 'Rogue', 'Necromancer', 'Druid']
RARITY = {'Legendary': 2.0, 'Rare': 17.5, 'Uncommon': 30.5, 'Common': 50.0}
SORCERER_ATTR = {'Strength', RARITY.get('Legendary'), 'Intelligence', RARITY.get('Common'), 'Dexerity', RARITY.get('Rare'), 'Willpower', RARITY.get('Common'), 'Vitality', RARITY.get('Uncommon')}

class CommonWeapon:
    id_iter = itertools.count(0)
    gen_attr_range = {'is_class': [6.0, 16.0], 'not_class': [4.0, 12.0]}

    def __init__(self):
        self.id = next(CommonWeapon.id_iter)

    def __repr__(self):
        return f'Weapon {self.id} created!'

print(__name__, type(__name__))

if __name__ == "__main__":
    while True:
        CHAR_CLASS = input('What is your class? ')
        if CHAR_CLASS in CLASSES:
            print(f'{CHAR_CLASS} is valid! Rolling weapons...')
            w1 = CommonWeapon()
            print(w1)
            w2 = CommonWeapon()
            print(w2)
            w3 = CommonWeapon()
            print(w3)
        else:
            print(f'{CHAR_CLASS} not valid. Breaking loop')
            break
