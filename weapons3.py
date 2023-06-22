CHAR_CLASS = ''
CLASSES = ['Barbarian', 'Sorcerer', 'Rogue', 'Necromancer', 'Druid']
RARITY = {'Legendary': 2.0, 'Rare': 17.5, 'Uncommon': 30.5, 'Common': 50.0}
GEN_ATTR = {'Strength', False, 'Intelligence', True, 'Dexerity', False, 'Willpower', False, 'Vitality', False}
GEN_ATTR_RNG = {'is_class': [6.0, 16.0], 'not_class': [4.0, 12.0]}

def roll_weapon(RARITY, GEN_ATTR):
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
            rolled = roll_weapon(RARITY, GEN_ATTR)
        else:
            pass
