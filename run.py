import os

def prompt():
    """
    Displays starting menu
    """
    print("\t\t\tWelcome to the DnD Text Adventure\n"
        "Explore the Dungeon, collect items, fight enemies and take on the Dungeon Lord.\n\n"
        "Actions:\t'move {direction}' (moves you North, East, South or West)\n"
        "\t\t'get {item}' (collect nearby items)\n"
        "\t\t'action {action}' (perform a corresponding action)\n\n")

    input("Press any key to continue...")

def clear():
    """
    Clears screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')

# Dictionary containing all the possible rooms for the game
# Each room is a key with directions corresponding to adjoining rooms
rooms = {
    'Lost Village' : {'North' : 'Haunted Mine', 'East' : 'Lumber Yard', 'South' : 'Howling Forest'},
    'Haunted Mine' : {'East' :  'Flooded Mineshaft', 'South' : 'Lost Village'},
    'Flooded Mineshaft' : {'West' : 'Haunted Mine', 'Item' : 'Holy Cross'},
    'Howling Forest' : {'North' : 'Lost Village', 'East' : 'Wolf Den', 'South' : 'Clear Spring'},
    'Wolf Den' : {'West' : 'Howling Forest', 'Item' : 'Faded Bible'},
    'Clear Spring' : {'North' : 'Howling Forest', 'Action' : 'Heal'},
    'Lumber Yard' : {'East' : 'Forbidden Grotto', 'West' : 'Lost Village'},
    'Forbidden Grotto' : {'North' : 'Cemetary', 'South' : 'Whispering Crypt', 'West' : 'Lumber Yard'},
    'Cemetary' : {'South' : 'Forbidden Grotto', 'Item' : 'Wooden Stake'},
    'Whispering Crypt' : {'North' : 'Forbidden Grotto', 'Boss' : 'Vampire'},
}

# List to track inventory items collected by the player
inventory = []

# Last move result
msg = ""

# Players current room
current_room = "Lost Village"

# List of vowels for correct grammar use in game
vowels = ['a', 'e', 'i', 'o', 'u']

def main():
    """
    Main Gameplay loop
    """
    while True:
        clear()

        # Display player info
        print(f"You find yourself in the {current_room}\nInventory: {inventory}\n{'-' * 27}")

        # Display msg
        print(msg)

        # Alerts player to a nearby item in current room
        if "Item" in rooms[current_room].keys():
            collectable_item = rooms[current_room]["Item"]

            if collectable_item not in inventory:
                # Correct grammar for vowel
                if collectable_item[0] in vowels:
                    print(f"You notice an {collectable_item} hidden nearby")
                # Correct grammar for consanant 
                else:
                    print(f"You notice a {collectable_item} hidden nearby")

        # Boss Fight
        if "Boss" in rooms[current_room].keys():

            # Difficult Fight
            if len(inventory) < 3:
                print(f"You are ill equipped to fight the {rooms[current_room]['Boss']}, prepare for a tough battle!")
                break

            # Easy Fight
            else:
                print(f"You are fully prepared to take on the {rooms[current_room]['Boss']}, this battle should be easy!")
                break

clear()
prompt()


