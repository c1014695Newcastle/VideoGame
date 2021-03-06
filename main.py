from InventoryViewer import InventoryViewer
import Tareth, Mia, William, Janet, Kitchen, Bedroom, ReusedCode
from ReusedCode import slow_print, checkn
from colorama import Fore

# use for main room

def start(inventory, progress):
    """Prints the starting screen and character description"""
    print("================================ Welcome to MURDER MANSION ================================\n")
    intro = "You are the friend of affluent industrialist Issac Hobbes and have been invited to his estate for a formal dinner to celebrate his engagement to Janet Hawthorne.\n\nThere are four other guests at this dinner: \n   - His son, William Hobbes \n   - His business partner, Tareth Codwen \n   - His daughter, Mia Hobbes\n   - His brother, Andrew Hobbes\nThe night is going well. You all sit around the grand dining room table as the dinner is being served. However, as Issac stands to make a toast to his fiance, he takes a sip of his wine and suddently starts to spit blood. You all watch as he convulses on the floor, spitting blood. Within moments, he is dead, and it is up to you to figure out who did it."
    slow_print(intro)
    main_room(inventory, progress)

def main_room(inventory, progress):
    choice = ""
    while choice != "8":
        slow_print( Fore.RESET + """
You are in the dining room -what would you like to do?
    1 - Talk to William
    2 - Talk to Tareth
    3 - Talk to Mia
    4 - Talk to Andrew
    5 - Talk to Janet
    6 - Head out to the hallway
    7 - View Inventory
    8 - ACCUSE\n""")
        choice = checkn(8)
        if choice == "1":
            # william()
            print("PLACE")
        elif choice == "2":
            Tareth.Tareth(inventory, progress)
        elif choice == "3":
            # mia()
            print("PLACE")
        elif choice == "4":
            # andrew()
            print("PLACE")
        elif choice == "5":
            Janet.Janet(inventory, progress)
            print("PLACE")
        elif choice == "6":
            # self.hallway()
            print("PLACE")
        elif choice == "7":
            InventoryViewer(inventory, progress)
        else:
            final_choice = input("""
    WARNING: THERE IS NO GOING BACK FROM THIS CHOICE - ARE YOU SURE THAT YOU ARE READY?
        1 - Yes
        2 - No
        
    > """)
            if final_choice == "1":
                #Accuse
                print("Place")
            else:
                choice = ""


def hallway(self):
        prompt = """
    You are now in the hallway - where would you like to go?
        1 - The kitchen
        2 - The Study
        3 - The Bedroom
        4 - Go Back\n"""
        slow_print(prompt)
        choice = checkn(4)
        if self.choice == "1":
            kitchen()
        elif self.choice == "2":
            study()
        elif self.choice == "3":
            bedroom()
        else:
            self.main_room()

# A list which contains key story events that are used in the accuse section of the game.
progress = {"Study Unlocked": 0, 
            "Tareth Janet": 0, "Tareth William": 0, "Tareth Mia": 0, "Tareth Andrew": 0, "Tareth Issac": 0, 
            "Janet Tareth": 0, "Janet William": 0, "Janet Mia": 0, "Janet Andrew": 0, "Janet Issac": 0,
            "William Tareth": 0, "William Janet": 0, "William Mia": 0, "William Andrew": 0, "William Issac": 0,
            "Mia Tareth": 0, "Mia William": 0, "Mia Janet": 0, "Mia Andrew": 0, "Mia Issac": 0,
            "Andrew Tareth": 0, "Andrew William": 0, "Andrew Mia": 0, "Andrew Andrew": 0, "Andrew Issac": 0
            }
# A list which contains every item you can collect during the game
inventory = {"Notepad": 0, "Study Key": 0, "Safe Pin": 0, "Contract": 0, "Scotch Bottle": 0, "Wine Bottle": 0, "Password": 0}

start(inventory, progress)
