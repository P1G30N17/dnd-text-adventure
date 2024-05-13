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

# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

clear()
prompt()