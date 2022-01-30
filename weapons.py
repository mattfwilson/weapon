# durability can be called twice in weight options
# Test?

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

SPECIALS = {
    'durability': 50,
    'damageUndead': 50,
    'increasedDmg': 40,
    'goldFind':35,
    'magicFind':35,  
    'lightningResist': 25,
    'fireResist': 25,
    'iceResist': 25,
    'chanceBlind': 20,
    'chanceSlow': 20,
    'socketed': 20,
    'criticalDmg': 20,
    'expGain': 15,
    'healthRegen':15, 
    'attackSpeed': 10,
    'criticalChance': 10,
    'meleeResist': 10,
    'magicResist': 10,
    'movementSpeed':8, 
    'manaLeech':8, 
    'healthLeech': 8,
    'legendaryFind': 5,
    'holy': 1,
    'cursed': 5
    }

COMMON_WEIGHTS = {1:60, 2:40, 3:5}    
UNCOMMON_WEIGHTS = {1:30, 2:20, 3:10}
RARE_WEIGHTS = {1:15, 2:25, 3:25, 4:8}
EPIC_WEIGHTS = {2:10, 3:35, 4:10, 5:3}
LEGENDARY_WEIGHTS = {3:10, 4:40, 5:25, 6:8}

def weightedRoll(weights, attributes):
    newRoll = random.choices(*zip(*weights.items()))
    # print(newRoll)
    attrRoll = random.choices(*zip(*attributes.items()), k=newRoll.pop())
    # print(attrRoll)
    return attrRoll

commonRoll = weightedRoll(COMMON_WEIGHTS, SPECIALS)
uncommonRoll = weightedRoll(UNCOMMON_WEIGHTS, SPECIALS)
rareRoll = weightedRoll(RARE_WEIGHTS, SPECIALS)
epicRoll = weightedRoll(EPIC_WEIGHTS, SPECIALS)
legendaryRoll = weightedRoll(LEGENDARY_WEIGHTS, SPECIALS)
print(f'Common roll: {commonRoll}')
print(f'Uncommon roll: {uncommonRoll}')
print(f'Rare roll: {rareRoll}')
print(f'Epic roll: {epicRoll}')
print(f'Legendary roll: {legendaryRoll}')


# SPECIALS_COUNT = {1:40, 2:20, 3:15, 4:8, 5:3}
# specialsCountRoll = random.choices(*zip(*SPECIALS_COUNT.items()))
# print(f'Roll for # of specials: {specialsCountRoll}')



# specialsRoll = random.choices(*zip(*SPECIALS.items()), k=specialsCountRoll.pop())
# print(f'Roll for types of specials: {specialsRoll}')


RARITIES2 = ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary']
weightedRoll2 = random.choices(RARITIES2, weights=[45, 20, 15, 8, 2], k=10)
print(f'Using weights: {weightedRoll2}')

