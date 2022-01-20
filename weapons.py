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

# class createWeapon:
#     def __init__(self, name, rarity, baseAttr, specials):
#         self.name = name
#         self.rarity = rarity
#         self.baseAttr = baseAttr
#         self.specials = specials
    
#     def __repr__(self):
#         return self.name

# if ROLL in range(0, 45):
#     weaponRoll = random.choice(COMMON)
#     print(f'You obtained a COMMON {weaponRoll}. ({ROLL})')
# elif ROLL in range(45, 75):
#     weaponRoll = random.choice(UNCOMMON)
#     print(f'You obtained an UNCOMMON {weaponRoll}. ({ROLL})')
# elif ROLL in range(75, 90):
#     weaponRoll = random.choice(RARE)
#     print(f'You obtained a RARE {weaponRoll}. ({ROLL})')
# elif ROLL in range(90, 98):
#     weaponRoll = random.choice(EPIC)
#     print(f'You obtained an EPIC {weaponRoll}. ({ROLL})')
# elif ROLL in range(98, 101):
#     weaponRoll = random.choice(LEGENDARY)
#     print(f'You obtained a LEGENDARY {weaponRoll}. ({ROLL})')

# item = createWeapon('Tubular Axe', 'Uncommon', ROLL, 'Movement Speed +7%')
# print(item.baseAttr)
# print(initialRoll())

# Test again
# test = [keys for keys, values in WEAPONS.items() if ROLL > values]
# print(test)

# RARITIES = {'Common':45, 'Uncommon':20, 'Rare':15, 'Epic':8, 'Legendary':2}
# weightedRoll = random.choices(*zip(*RARITIES.items()), k=10)
# print(f'Using zip: {weightedRoll}')

SPECIALS_COUNT = {1:40, 2:20, 3:15, 4:8, 5:5}
specialsCountRoll = random.choices(*zip(*SPECIALS_COUNT.items()))
print(f'Roll for # of specials: {specialsCountRoll}')


SPECIALS = {
    'durability': 50,
    'damageUndead': 50,
    'goldFind':35,
    'magicFind':35,  
    'lightningResist': 25,
    'fireResist': 25,
    'iceResist': 25,
    'socketed': 20,
    'criticalHitDmg': 20,
    'expGain': 15,
    'attackSpeed': 10,
    'criticalChance': 10,
    'meleeResist': 10,
    'magicResist': 10,
    'movementSpeed':8, 
    'healthRegen':8, 
    'manaLeech':8 
    }

specialsRoll = random.choices(*zip(*SPECIALS.items()), k=specialsCountRoll.pop())
print(f'Roll for types of specials: {specialsRoll}')


# RARITIES2 = ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary']
# weightedRoll2 = random.choices(RARITIES2, weights=[45, 20, 15, 8, 2], k=10)
# print(f'Using weights: {weightedRoll2}')

