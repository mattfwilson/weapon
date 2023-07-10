sor_adj = {
    'Common': ['Basic', 'Apprentice', 'Feeble', 'Sturdy', 'Oak', 'Hewn'],
    'Magic': ['Enchanted', 'Enlightened', 'Fanatic\'s', 'Aged', 'Assistant\'s'],
    'Rare': ['Cleric\'s', 'Undying', 'Apostle\'s', 'Choker\'s', 'Elder\'s', 'Brutal'],
    'Legendary': ['Empowered', 'Tribal', 'Elemental', 'Blasphemy', 'Tortured'],
    'Unique': ['Sacred', 'Intellect\'s', 'Cultist\'s', 'Jambiya\'s', 'Serpentine']
    }
sor_weap = ['Wand', 'Staff', 'Dagger', 'Edge']

sor_attrs = ['Intelligence', 'Willpower', 'Dexterity', 'Vitality', 'Strength']
public_attrs = {
    'Common': {
        'Poison Resistance': True,
        'Cold Resistance': True,
        'Fire Resistance': True,
        'Lightning Resistance': True,
        'Shadow Resistance': True,
        'Undead Resistance': True
        },
    'Magic': {
        'Armor': False,
        'Dodge Chance': True,
        'Healing from Potions': False,
        'Basic Skill Damage': True,
        'Crowd Control Duration': True,
        'Crowd Control Damage': True,
        'Healing Received': False,
        'Thorns': False
        },
    'Rare': {
        'Maximum Life': False,
        'Overpower Chance': True,
        'Overpower Damage': True,
        'Critical Strike Chance': True,
        'Critical Strike Damage': True,
        'Damage vs Controlled': True,
        'Damage': True,
        'Ultimate Skill Damage': True,
        'Core Skill Damage': True,
        'Cooldown Reduction': True
        },
    'Legendary': {
        'Damage with Skills', 'Damage vs Elites', 'Life on Kill', 'Critical Strike Chance', 'All Stats'},
    'Unique': {
        'Movement Speed': True,
        'Weapon Damage': True,
        'Weapon Speed': True,
        'Vulnerable Damage': True,
        'Resist All': True,
        'Attack Speed': True,
        'Lucky Hit Chance': True,
        }
    }

perc_attr = {
    'Common': [4.0, 8.0],
    'Magic': [6.0, 10.0],
    'Rare': [8.5, 16.0],
    'Legendary': [10.0, 18.0],
    'Unique': [14.0, 20.0]
    }
