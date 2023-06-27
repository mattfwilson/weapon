import itertools
import random

char_class = str()
char_level = 1
inventory = []
classes = ['Barbarian', 'Sorcerer', 'Rogue', 'Necromancer', 'Druid']
rarity = {'Legendary': 3, 'Rare': 17, 'Uncommon': 30, 'Common': 50}
sor_attr = {'Strength', rarity.get('Legendary'), 'Intelligence', rarity.get('Common'), 'Dexerity', rarity.get('Rare'), 'Willpower', rarity.get('Common'), 'Vitality', rarity.get('Uncommon')}

sor_weap_type = ['Wand', 'Staff', 'Dagger']
sor_common_adj = ['Basic', 'Apprentice', 'Feeble', 'Sturdy', 'Oak']
sor_uncommon_adj = ['Enchanted', 'Enlightened', 'Fanatic\'s']
sor_rare_adj = ['Cleric\'s', 'Undying', 'Apostle\'s']
sor_legendary_adj = ['Sacred', 'Awkward', 'Elementalist\'s']

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
        inventory.append(self._drop)

    def __repr__(self):
        return f'{str(self._adj)} {str(self._weapon)}'

    def get_item_level(self):
        return self._item_level
    
if __name__ == "__main__":
    char_class = 'Sorcerer'
    if char_class in classes:
        print(f'You are a {char_class}! Rolling weapon...')
        common1 = Common(sor_weap_type, sor_common_adj)
        print(f'Inventory: {inventory}')
        print(f'{common1}, Lvl: {common1.get_item_level()}')
    else:
        print(f'{char_class} is not a valid class. Exiting...')
