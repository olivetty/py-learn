import time, os, random

# just to have color on print
start_color = "\033[31;3m"
end_color = "\033[m"


# generate a number between 1 and side
def roll_dice(sides):
    return random.randint(1, sides)


# generates a countdown to make the user think is doing something
def countdown(t):
    for i in range(t):
        os.system("clear")
        print(f"Generating in: {i}s")
        time.sleep(1)


character_name = ["Aang", "Katara", "Sokka", "Toph", "Zuko"]
character_type = ["human", "elf", "orc", "wizard", "demon"]


def generate_char_type():  # generates a character type from allowed types
    return character_type[random.randint(0, (len(character_type) - 1))]


def generate_char_name():  # generates a character name from allowed names
    return character_name[random.randint(0, (len(character_name) - 1))]


# generating the character
def generate_character():
    # generate the character
    name = generate_char_name()
    type = generate_char_type()
    health = (roll_dice(6) * roll_dice(12)) / 2 + 10
    strength = (roll_dice(6) * roll_dice(12)) / 2 + 12

    # fake loading
    countdown(2)
    os.system("clear")

    # show the character to the user
    print(f"NAME: {start_color}{name}{end_color}")
    print(f"RACE: {start_color}{type}{end_color}")
    print(f"HEALTH: {start_color} {health} {end_color}")
    print(f"STRENGTH: {start_color} {strength} {end_color}")

    # return the character as global in order to be used outside the function
    global player_char
    player_char = {"name": name, "type": type, "health": health, "strength": strength}


# keep or discard the character
generate_character()
while input("Keep this character? (y/n) ") == "n":
    generate_character()
else:
    print(player_char)

# rename the character
if input("Do you want to rename your character (y/n) ") == "y":
    os.system("clear")
    player_char["name"] = input("New character name? ")
    os.system("clear")
    print(f"Your Character: {player_char}")
else:
    print("Let the adventure begin!")
