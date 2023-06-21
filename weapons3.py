CHAR_CLASS = ''
RARITY = {'Legendary': 2.0, 'Rare': 17.5, 'Uncommon': 30.5, 'Common': 50.0}
GEN_ATTR = {'Strength', False, 'Intelligence', True, 'Dexerity', False, 'Willpower', False, 'Vitality', False}
GEN_ATTR_RNG = {'is_class': [6.0, 16.0], 'not_class': [4.0, 12.0]}

CHAR_CLASS = input('What is your class? ')
ROLL = ''

def main():
    while True:
        if ROLL == 'y':
            rarity = random.choice(RARITY)
            attribute = random.choice(GEN_ATTR)
            print(f'Rarity: {rarity}, Attribute: {attribute}')
        elif ROLL == 'n':
            quit()
        else:
            roll = input('Roll weapon? (y/n) ')

if __name__ == "__main__":
    main()
