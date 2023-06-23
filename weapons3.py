import itertools

CHAR_CLASS = ''
CHAR_LEVEL = 1
CLASSES = ['Barbarian', 'Sorcerer', 'Rogue', 'Necromancer', 'Druid']
RARITY = {'Legendary': 2.0, 'Rare': 17.5, 'Uncommon': 30.5, 'Common': 50.0}
GEN_ATTR = {'Strength', False, 'Intelligence', True, 'Dexerity', False, 'Willpower', False, 'Vitality', False}

class CommonWeapon:
    id = itertools.count(0)
    gen_attr_range = {
        'is_class': [6.0, 16.0],
        'not_class': [4.0, 12.0]
        }

    def __init__(self):
        self.id = next(CommonWeapon.id)

    def __repr__(self):
        return f'Weapon {self.id} created!'

w1 = CommonWeapon()
print(w1)

def roll_weapon(RARITY):
    roll = ''
    if roll == 'y':
        rarity = random.choice(RARITY)
        attribute = random.choice(GEN_ATTR)
        print(f'Rarity: {rarity}, Attribute: {attribute}')
    elif roll == 'n':
        quit()
    else:
        roll = input('Roll weapon? (y/n) ')

print(__name__, type(__name__))

if __name__ == "__main__":
    while True:
        CHAR_CLASS = input('What is your class? ')
        if CHAR_CLASS in CLASSES:
            rolled = roll_weapon(RARITY)
            print(f'{rolled}: (rolled func executed)')
        else:
            print(f'Breaking loop')
            break
