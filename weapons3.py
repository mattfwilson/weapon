import itertools
import random

char_class = str()
char_level = 1
inventory = []
classes = ['Barbarian', 'Sorcerer', 'Rogue', 'Necromancer', 'Druid']
rarity = {'Legendary': 3, 'Rare': 17, 'Uncommon': 30, 'Common': 50}
sor_attr = {'Strength', rarity.get('Legendary'), 'Intelligence', rarity.get('Common'), 'Dexerity', rarity.get('Rare'), 'Willpower', rarity.get('Common'), 'Vitality', rarity.get('Uncommon')}

sor_weap = ['Wand', 'Staff']
sor_common_adj = ['Basic', 'Apprentice', 'Feeble']
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
        self.item_level = self.id + 1
        self.weapon = random.choices(weapon, cum_weights=(0.50, 0.50))
        self.adj = random.choices(common_adj, cum_weights=(0.50, 0.35, 0.15))
        print(f'{str(self.adj)} {str(self.weapon)}')
        inventory.append(self)

    def __repr__(self):
        return f'Weapon {self.id}'

    def get_item_level(self):
        return self.item_level

if __name__ == "__main__":
    char_class = 'Sorcerer'
    if char_class in classes:
        print(f'You are a {char_class}! Rolling weapon...')
        common1 = Common(sor_weap, sor_common_adj)
        print(f'Inventory: {inventory}')
        print(f'{common1}, Item Level: {common1.get_item_level()}')
    else:
        print(f'{char_class} is not a valid class. Exiting...')
