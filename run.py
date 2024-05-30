import os

# Dictionary containing all the possible rooms for the game
# Each room is a key with directions corresponding to adjoining rooms
rooms = {
    'Lost Village' : {'North' : 'Haunted Mine', 'East' : 'Lumber Yard', 'South' : 'Howling Forest'},
    'Haunted Mine' : {'East' :  'Flooded Mineshaft', 'South' : 'Lost Village'},
    'Flooded Mineshaft' : {'West' : 'Haunted Mine', 'Item' : 'Holy Cross'},
    'Howling Forest' : {'North' : 'Lost Village', 'East' : 'Wolf Den', 'South' : 'Clear Spring'},
    'Wolf Den' : {'West' : 'Howling Forest', 'Item' : 'Bible'},
    'Clear Spring' : {'North' : 'Howling Forest', 'Action' : 'Crumbling Shrine'},
    'Lumber Yard' : {'East' : 'Forbidden Grotto', 'West' : 'Lost Village', 'Item': 'Axe'},
    'Forbidden Grotto' : {'North' : 'Cemetary', 'South' : 'Whispering Crypt', 'West' : 'Lumber Yard', 'Item' : 'Crypt Key'},
    'Cemetary' : {'South' : 'Forbidden Grotto', 'Item' : 'Wooden Stake'},
    'Whispering Crypt' : {'North' : 'Forbidden Grotto', 'Boss' : 'Ancient Vampire'},
}

# List to track inventory items collected by the player
inventory = []

# List of vowels for correct grammar use in game
vowels = ['A', 'E', 'I', 'O', 'U']


def prompt():
    """
    Displays starting menu
    """
    print("\t\t\tWelcome to the DnD Text Adventure\n"
        "Explore the Dungeon, collect all the  hidden items and a blessing\n"
        "Finally face the Vampire that has been terrorising your local village to win.\n\n"
        "Actions:\t'move {direction}' (moves you North, East, South or West)\n"
        "\t\t'get {item}' (collect nearby items)\n"
        "\t\t'use {environment}' (use a terrain feature)\n"
        "\t\t'exit (Exit the game at any time)\n\n")

    input("Press ENTER to continue...\n")


def clear():
    """
    Clears screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def player_help():
    """
    Displays help menu
    """
    clear()
    print("Actions:'move {direction}' (moves you North, East, South or West)\n"
        "\t'get {item}' (collect nearby items)\n"
        "\t'use {environment}' (use a terrain feature)\n"
        "\t'exit (Exit the game at any time)\n\n")

    input("Press ENTER to continue...\n")


def game_over(player_input):
    if player_input == "Yes":
        inventory.clear()
        main()
    elif player_input == "Exit":
        exit()
    else:
        print("Invalid Input, Please enter 'Yes' to play again or 'Exit' to quit")


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
        print(f"You find yourself in the {current_room}\nAvailable Interactions: {list(rooms[current_room].keys())}\nInventory: {inventory}\n{'-' * 27}")

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

            # Failure
            if len(inventory) < 6:
                print(f"You are not equipped to fight the {rooms[current_room]['Boss']}, prepare for a tough battle!")
                print("The Ancient Vampire, rises from its crypt, only to instantly appear behind you,\n"
                    "tearing into your neck with its razor sharp fangs and draining you of your precious lifeblood!")
                input()
                clear()
                print("GAME OVER\nWould you like to try again?\n'Yes' to play again, 'Exit' to quit\n")
                player_input = input("\n").title()
                game_over(player_input)

            # Victory
            else:
                print(f"You are fully prepared to take on the {rooms[current_room]['Boss']}, this battle should be easy!")
                input()
                clear()
                print("The Ancient Vampire, rises from its crypt, only to instantly appear behind you, trying to rip into your neck to bleed you dry!\n"
                    "Luckily your blessing of Protection repels the Vampire Lord, stunning him in the process!\n"
                    "You use this chance to your advantage, using all the items you have gathered throughout your quest to thwart the Vampire Lords every attack!\n"
                    "Finally drained of its vigor the Vampire Lord flees to his coffin, where you are able to finally plunge the Wooden Stake into its undead heart!")
                print("CONGRATULATIONS! You saved your village from the terror of the Vampire Lord!\nWould you like to play again?\n'Yes' to play again, 'Exit' to quit\n")
                player_input = input("\n").title()
                game_over(player_input)
                

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
                    if "Blessing of Protection" not in inventory:
                        msg = f"The shrine glows with holy light, and  you recieve a blessing of protection from a forgotten deity from a time long lost!"
                        inventory.append("Blessing of Protection")
                    else:
                        msg = "The shrine's power already radiates through you"
                else:
                    msg = f"{item} is not possible."
            except:
                msg = f"{item} is not possible."
        
        # Displays help prompt
        elif action == "Help":
            player_help()
        
        # Exit the game
        elif action == "Exit":
            exit()
        
        # Any other invalid input from player
        else:
            msg = "Invalid command."


clear()
prompt()
main()
