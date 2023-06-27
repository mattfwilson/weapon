import itertools
import random

CHAR_CLASS = str()
CHAR_LEVEL = 1
INVENTORY = []
CLASSES = ['Barbarian', 'Sorcerer', 'Rogue', 'Necromancer', 'Druid']
RARITY = {'Legendary': 3, 'Rare': 17, 'Uncommon': 30, 'Common': 50}
SOR_ATTR = {'Strength', RARITY.get('Legendary'), 'Intelligence', RARITY.get('Common'), 'Dexerity', RARITY.get('Rare'), 'Willpower', RARITY.get('Common'), 'Vitality', RARITY.get('Uncommon')}

SOR_WEAP = ['Wand', 'Staff']
SOR_COMMON_ADJ = ['Basic', 'Apprentice', 'Feeble']
SOR_UNCOMMON_ADJ = ['Enchanted', 'Enlightened', 'Fanatic\'s']
SOR_RARE_ADJ = ['Cleric\'s', 'Undying', 'Apostle\'s']
SOR_LEGENDARY_ADJ = ['Sacred', 'Awkward', 'Elementalist\'s']

class Weapon:
    id_iter = itertools.count(1)
    def __init__(self):
        self.id = next(Weapon.id_iter)

class Common(Weapon):
    def __init__(self, weapon, common_adj):
        super().__init__()
        self.item_level = self.id + 1
        self.weapon = random.choices(weapon, cum_weights=(0.50, 0.50))
        self.adj = random.choices(common_adj, cum_weights=(0.50, 0.35, 0.15))
        print(f'{str(self.adj)} {str(self.weapon)}')
        INVENTORY.append(self)

    def __repr__(self):
        return f'Weapon {self.id}'

    def get_item_level(self):
        return self.item_level

if __name__ == "__main__":
    CHAR_CLASS = 'Sorcerer'
    if CHAR_CLASS in CLASSES:
        print(f'You are a {CHAR_CLASS}! Rolling weapon...')
        common1 = Common(SOR_WEAP, SOR_COMMON_ADJ)
        print(f'Inventory: {INVENTORY}')
        print(f'{common1}, Item Level: {common1.get_item_level()}')
    else:
        print(f'{CHAR_CLASS} is not a valid class. Exiting...')
