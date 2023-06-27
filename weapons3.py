import itertools
import random

CHAR_CLASS = str()
CHAR_LEVEL = 1
INVENTORY = []
CLASSES = ['Barbarian', 'Sorcerer', 'Rogue', 'Necromancer', 'Druid']
RARITY = {'Legendary': 3, 'Rare': 17, 'Uncommon': 30, 'Common': 50}

sor_weap_type = ['Wand', 'Staff', 'Dagger']
sor_common_adj = ['Basic', 'Apprentice', 'Feeble', 'Sturdy', 'Oak']
sor_uncommon_adj = ['Enchanted', 'Enlightened', 'Fanatic\'s']
sor_rare_adj = ['Cleric\'s', 'Undying', 'Apostle\'s']
sor_legendary_adj = ['Sacred', 'Awkward', 'Elementalist\'s']
sor_attr = {'Strength', RARITY.get('Legendary'), 'Intelligence', RARITY.get('Common'), 'Dexerity', RARITY.get('Rare'), 'Willpower', RARITY.get('Common'), 'Vitality', RARITY.get('Uncommon')}

class Weapon:
    id_iter = itertools.count(1)
    def __init__(self):
        self.id = next(Weapon.id_iter)

class Common(Weapon):
    def __init__(self, weapon, common_adj):
        super().__init__()
        self._item_level = self.id + 1
        self._weapon = ', '.join(random.choices(weapon))
        self._adj = ', '.join(random.choices(common_adj))
        self._drop = self._adj + ' ' + self._weapon
        INVENTORY.append(self._drop)

    def __repr__(self):
        return f'{str(self._adj)} {str(self._weapon)}'

    def get_item_level(self):
        return self._item_level
    
if __name__ == "__main__":
    CHAR_CLASS = 'Sorcerer'
    if CHAR_CLASS in CLASSES:
        print(f'You are a {CHAR_CLASS}! Rolling weapon...')
        common1 = Common(sor_weap_type, sor_common_adj)
        print(f'INVENTORY: {INVENTORY}')
        print(f'{common1}, Lvl: {common1.get_item_level()}')
    else:
        print(f'{CHAR_CLASS} is not a valid class. Exiting...')
