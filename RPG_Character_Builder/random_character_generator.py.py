import data
import random

# The Charaacter Model
class Character:
    c_strength = 10
    c_dexterity = 10
    c_constitution = 10
    c_intelligence = 10
    c_wisdom = 10
    c_charisma = 10

    c_race = "Human"
    c_class = "Fighter"
    c_firstname = "Jack"
    c_lastname = "Petty"
    c_weapon = ["Dagger"]
    c_armor = ["Cloth shirt"]
    c_skills = ["Insight"]
    c_abilities = ["Rage"]
    c_spells = ["None"]
    c_hp = 1
    c_gold = 0
    c_background = "outlander"
    c_saving_throws = []
    c_racial_traits = []

    c_age = 18
    c_size = "Medium"

    c_languages = ["Common"]
    c_hair_color = "brown"
    c_hair_type = "Wavy"
    c_eye_color = "brown"

    c_appearance = []
    c_traits = []
    c_mannerisms = []
    c_talents = []

    # its a good idea to include a way of representing the object as a string
    def __str__(self):
        return "A {} {} named {}.".format(self.c_race, self.c_class, self.c_firstname)

# A function to simulate rolling 4 six sided dice and adding the three highest
# numbers together.

def RollStat():
    dice = []
    # roll 4 six sided dice.
    for i in range(4):
        dice.append(random.randrange(1,7))

    total = 0
    lowest = dice[0]

    # find the lowest value
    for num in dice:
        if num < lowest:
            lowest = num

    # add all the dice and subtract the lowest value
    for num in dice:
        total += num

    return total - lowest

# The main part of our program. This will handle all the random creation
# necessary for creating the character.
def CreateNewCharacter():
    new_character = Character();

    races = []
    classes = []

    for race in data.races:
        races.append(race)

    for _class in data.classes:
        classes.append(_class)

    new_character.c_race = races[random.randrange(0,len(races))]
    new_character.c_class = classes[random.randrange(0,len(classes))]

    # names are the most complicated part. Special cases are needed
    firstnames = []
    lastnames = []

    # Humnas have different ethnic groups and various naming conventions for
    # those groups. We've called them 'type' here.
    if new_character.c_race == 'Human':
        types = []

        for type in data.races['Human']['first names']:
            types.append(type)

        type = types[random.randrange(0,len(types))]

        for name in data.races[new_character.c_race]['first names'][type]:
            firstnames.append(name)

        for name in data.races[new_character.c_race]['last names'][type]:
            lastnames.append(name)

    elif new_character.c_race == "Half-Elf":
        types = []

        for type in data.races['Human']['first names']:
            types.append(type)

        type = types[random.randrange(0,len(types))]

        for name in data.races['Human']['first names'][type]:
            firstnames.append(name)

        for name in data.races['Elf']['first names']:
            firstnames.append(name)

        for name in data.races['Human']['last names'][type]:
            lastnames.append(name)

        for name in data.races['Elf']['last names']:
            lastnames.append(name)

    else:
        for name in data.races[new_character.c_race]['first names']:
            firstnames.append(name)

        if new_character.c_race == "Half-Orc":
            pass
        else:
            for name in data.races[new_character.c_race]['last names']:
                lastnames.append(name)

    new_character.c_firstname = firstnames[random.randrange(0,len(firstnames))]

    if new_character.c_race != "Half-Orc":
        new_character.c_lastname = lastnames[random.randrange(0,len(lastnames))]

    # roll the character stats
    new_character.c_strength = RollStat()
    new_character.c_dexterity = RollStat()
    new_character.c_constitution = RollStat()
    new_character.c_intelligence = RollStat()
    new_character.c_wisdom = RollStat()
    new_character.c_charisma = RollStat()

    weapons = []
    armors = []

    for weapon in data.classes[new_character.c_class]['weapons']:
        weapons.append(weapon)

    new_character.c_weapon = weapons[random.randrange(0,len(weapons))]

    for armor in data.classes[new_character.c_class]['armor']:
        armors.append(armor)

    new_character.c_armor = armors[random.randrange(0,len(armors))]

    new_character.c_skills = data.classes[new_character.c_class]['skills']

    if 'spells' in data.classes[new_character.c_class]:
        new_character.c_spells =  data.classes[new_character.c_class]['spells']

    new_character.c_abilities =  data.classes[new_character.c_class]['abilities']
    new_character.c_background = data.classes[new_character.c_class]['background']
    new_character.c_languages = ["Common"]
    new_character.c_languages += data.races[new_character.c_race]['languages']
    new_character.c_racial_traits = data.races[new_character.c_race]['traits']

    mannerisms = []
    for mannerism in data.mannerisms:
        mannerisms.append(mannerism)
    new_character.c_mannerisms = mannerisms[random.randrange(0,len(mannerisms))]

    traits = []
    for trait in data.traits:
        traits.append(trait)
    new_character.c_traits = traits[random.randrange(0,len(traits))]

    talents = []
    for talent in data.talents:
        talents.append(talent)
    new_character.c_talent = talents[random.randrange(0,len(talents))]

    appearances = []
    for appearance in data.appearance:
        appearances.append(appearance)
    new_character.c_appearance = appearances[random.randrange(0,len(appearances))]


    # There are some minor differences in how we'll present the data, depending
    # on the race involved. For instance, "An Elf" vs "A Human."
    if new_character.c_race == "Half-Orc":
        print("A {} {} named {}.".format(new_character.c_race, new_character.c_class, new_character.c_firstname))
    elif new_character.c_race == "Elf":
        print("An {} {} named {} {}.".format(new_character.c_race, new_character.c_class, new_character.c_firstname, new_character.c_lastname))
    else:
        print("A {} {} named {} {}.".format(new_character.c_race, new_character.c_class, new_character.c_firstname, new_character.c_lastname))

    print("Strength: {} Dexterity: {} Constitution: {} Intelligence: {} Wisdom: {} Charisma: {}".format(
        new_character.c_strength, new_character.c_dexterity,new_character.c_constitution,
        new_character.c_intelligence, new_character.c_wisdom, new_character.c_charisma))

    print("Background: " + new_character.c_background + ", Languages: " + str(new_character.c_languages))
    print("\nWeapon: " + new_character.c_weapon + ", Armor: " + new_character.c_armor)
    print("Skills: " + str(new_character.c_skills))
    print("Abilities: " + str(new_character.c_abilities))
    print("Spells: " + str(new_character.c_spells))
    print("Traits: " + str(new_character.c_racial_traits))

    print("\nMannerisms: " + str(new_character.c_mannerisms))
    print("Personality Traits: " + str(new_character.c_traits))
    print("Talents: " + str(new_character.c_talent))
    print("Appearance: " + str(new_character.c_appearance))
    print("\n")


# This is the entry point for the program
print("Welcome to the Random Character Generator.")

new_input = ""

while new_input != "quit":
    new_input = input("Create a new character?: ")

    new_input = new_input.lower()
    if new_input == "yes" or new_input == "y":
        print("Ok, let's make a character!\n")
        print("===============================================================")
        CreateNewCharacter()
    elif new_input == "no" or new_input == "n" or new_input == "quit":
        new_input = "quit"
        print("Goodbye!")
