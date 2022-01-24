# fix durability being able to be called twice in weighted options

import random

# global vars
ROLL = 0

# names
FIRST_NAME = ['Holy', 'Wicked', 'Corrupted']
LAST_NAME = ['Smite', 'Anguish', 'Revenge']

# rarities
COMMON = ['Sword', 'Axe', 'Great Axe', 'Dagger', 'Shiv']
UNCOMMON = ['Sabre', 'Longbow', 'Mace', 'Cudgel', 'Spear', 'Hammer']
RARE = ['Scimitar', 'Lance', 'Knuckles', 'Flail']
EPIC = ['Crossbow', 'Quarterstaff']
LEGENDARY = ['Machine Gun', 'Whip']
ATTRIBUTES = ['STR', 'DEX', 'INT', 'VIT', 'CHR']

# attributes
COMMON_ATT = {
    'durability': 50,
    'damageUndead': 50,
    'increasedDmg': 30,
    'goldFind':35,
    'magicFind':35,  
    'chanceBlind': 20,
    'chanceSlow': 20,
    'socketed': 20,
    'criticalDmg': 20,
    'expGain': 15,
    'healthRegen':15, 
    }

RARE_ATT = {
    'durability': 40,
    'goldFind':35,
    'magicFind':35,  
    'chanceBlind': 20,
    'chanceSlow': 20,
    'socketed': 20,
    'criticalDmg': 10,
    'expGain': 15,
    'healthRegen':15, 
    'attackSpeed': 10,
    'criticalChance': 10,
    'movementSpeed':8, 
    }

LEGENDARY_ATT = {
    'increasedDmg': 50,
    'lightningResist': 25,
    'fireResist': 25,
    'iceResist': 25,
    'chanceBlind': 20,
    'chanceSlow': 20,
    'durability': 20,
    'socketed': 25,
    'criticalDmg': 15,
    'healthRegen':15, 
    'attackSpeed': 15,
    'criticalChance': 15,
    'meleeResist': 10,
    'magicResist': 10,
    'movementSpeed':8, 
    'manaLeech':10, 
    'healthLeech': 8,
    'legendaryFind': 5,
    'baseAttr+': 5,
    'holy': 2,
    'cursed': 1
    }

COMMON_WEIGHTS = {1:60, 2:40, 3:5}    
UNCOMMON_WEIGHTS = {1:30, 2:40, 3:5}
RARE_WEIGHTS = {2:40, 3:25, 4:8}
EPIC_WEIGHTS = {2:10, 3:45, 4:20, 5:3}
LEGENDARY_WEIGHTS = {3:5, 4:40, 5:25, 6:8}
GODLY_WEIGHTS = {5:10, 6:5}

def rarity_roll():
    RARITIES = ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Godly']
    weightedRoll = random.choices(RARITIES, weights=[28, 28, 18, 10, 10, 10])
    return weightedRoll

def attribute_roll(weights, attributes):
    newRoll = random.choices(*zip(*weights.items()))
    attrRoll = random.choices(*zip(*attributes.items()), k=newRoll.pop())
    return attrRoll

rollRarity = rarity_roll()
print(rollRarity)

if rollRarity[0] == 'Common':
    commonRoll = attribute_roll(COMMON_WEIGHTS, COMMON_ATT)
    print(f'Common attribute roll: {commonRoll}')
elif rollRarity[0] == 'Uncommon':
    uncommonRoll = attribute_roll(UNCOMMON_WEIGHTS, COMMON_ATT)
    print(f'Uncommon attribute roll: {uncommonRoll}')
elif rollRarity[0] == 'Rare':
    rareRoll = attribute_roll(RARE_WEIGHTS, RARE_ATT)
    print(f'Rare attribute roll: {rareRoll}')
elif rollRarity[0] == 'Epic':
    epicRoll = attribute_roll(EPIC_WEIGHTS, RARE_ATT)
    print(f'Epic attribute roll: {epicRoll}')
elif rollRarity[0] == 'Legendary':
    legendaryRoll = attribute_roll(LEGENDARY_WEIGHTS, LEGENDARY_ATT)
    print(f'Legendary attribute roll: {legendaryRoll}')
elif rollRarity[0] == 'Godly':
    godlyRoll = attribute_roll(GODLY_WEIGHTS, LEGENDARY_ATT)
    print(f'Legendary attribute roll: {godlyRoll}')



