import os

def prompt():
    """
    Displays starting menu
    """
    print("\t\t\tWelcome to the DnD Text Adventure\n"
        "Explore the Dungeon, collect items, fight enemies and take on the Dungeon Lord.\n\n"
        "Actions:\t'move {direction}' (moves you North, East, South or West)\n"
        "\t\t'get {item}' (collect nearby items)\n\n")

    input("Press any key to continue...")

def clear():
    """
    Clears screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')
