import random

# Global Vars
ROLL = 0

# Names
FIRST = ['Holy', 'Wicked', 'Corrupted']
LAST = ['Smite', 'Anguish', 'Revenge']

# Rarities
COMMON = ['Sword', 'Axe', 'Great Axe', 'Dagger', 'Shiv']
UNCOMMON = ['Sabre', 'Longbow', 'Mace', 'Cudgel', 'Spear', 'Hammer']
RARE = ['Scimitar', 'Lance', 'Knuckles', 'Flail']
EPIC = ['Crossbow', 'Quarterstaff']
LEGENDARY = ['Machine Gun', 'Whip']

ATTRIBUTES = ['STR', 'DEX', 'INT', 'VIT', 'CHR']

def initialRoll():
    nameRoll = random.randint(1, 100)
    rarityRoll = random.randint(1, 100)
    baseAttrRoll = random.randint(1, 100)
    specialsRoll = random.randint(1, 100)
    return nameRoll, rarityRoll, baseAttrRoll, specialsRoll

def roll():
    randomRoll = random.randint(1, 100)
    return randomRoll

ROLL = roll()

class createWeapon:
    def __init__(self, name, rarity, baseAttr, specials):
        self.name = name
        self.rarity = rarity
        self.baseAttr = baseAttr
        self.specials = specials
    
    def __repr__(self):
        return self.name

if ROLL in range(0, 45):
    weaponRoll = random.choice(COMMON)
    print(f'You obtained a COMMON {weaponRoll}. ({ROLL})')
elif ROLL in range(45, 75):
    weaponRoll = random.choice(UNCOMMON)
    print(f'You obtained an UNCOMMON {weaponRoll}. ({ROLL})')
elif ROLL in range(75, 90):
    weaponRoll = random.choice(RARE)
    print(f'You obtained a RARE {weaponRoll}. ({ROLL})')
elif ROLL in range(90, 98):
    weaponRoll = random.choice(EPIC)
    print(f'You obtained an EPIC {weaponRoll}. ({ROLL})')
elif ROLL in range(98, 101):
    weaponRoll = random.choice(LEGENDARY)
    print(f'You obtained a LEGENDARY {weaponRoll}. ({ROLL})')

item = createWeapon('Tubular Axe', 'Uncommon', ROLL, 'Movement Speed +7%')
print(item.baseAttr)
print(initialRoll())

# Test again
# test = [keys for keys, values in WEAPONS.items() if ROLL > values]
# print(test)
 
