import os

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

# List of vowels for correct grammar use in game
vowels = ['a', 'e', 'i', 'o', 'u']

def prompt():
    """
    Displays starting menu
    """
    print("\t\t\tWelcome to the DnD Text Adventure\n"
        "Explore the Dungeon, collect items, fight enemies and take on the Dungeon Lord.\n\n"
        "Actions:\t'move {direction}' (moves you North, East, South or West)\n"
        "\t\t'get {item}' (collect nearby items)\n"
        "\t\t'fight {monster}' (fight the monster)\n"
        "\t\t'flee {monster}' (flee combat to prevous location)\n"
        "\t\t'use {environment}' (use a terrain feature)\n"
        "\t\t'exit (Exit the game at any time)\n\n")

    input("Press any key to continue...")

def clear():
    """
    Clears screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """
    Main Gameplay loop
    """
    # Last move result
    msg = ""

    # Players current room
    current_room = "Lost Village"

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
        
        # Alerts player to an interactable event
        if "Action" in rooms[current_room].keys():
            useable_item = rooms[current_room]["Action"]
            print(f"You notice a {useable_item} nearby")
                    

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

        # Accepts the players input as an action
        player_input = input("Perform an action:\n")

        # Splits player action into words
        next_action = player_input.split(" ")

        # First word becomes the players action
        action = next_action[0].title()
        if len(next_action) > 1:
            item = next_action[1:]
            item = ' '.join(item).title()
            direction = next_action[1].title()

        # Moving between rooms
        if action == "Move":
            try:
                current_room = rooms[current_room][direction]
                msg = f"You move {direction}."
            except: 
                msg = "There is no clear path that way"

        # Getting an item
        elif action == "Get":
            try:
                if item == rooms[current_room]["Item"]:
                    if item not in inventory:
                        inventory.append(rooms[current_room]["Item"])
                        msg = f"You added {item} to your inventory!"
                    else:
                        msg = f"You already collected the {item} previously."
                else:
                    msg = f"{item} is not located here."
            except:
                msg = f"{item} is not located here."

        # Using an environment feature
        elif action == "Use":
            try:
                if item == rooms[current_room]["Action"]:
                    msg = f"You successfully used {item}!"
                else:
                    msg = f"{item} is not possible."
            except:
                msg = f"{item} is not possible."
        
        # Exit the game
        elif action == "Exit":
            break
        
        # Any other invalid input from player
        else:
            msg = "Invalid command."

            

clear()
prompt()
main()


