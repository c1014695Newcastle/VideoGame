import sys,time,os, Tareth, Mia, William, Janet, Study, Kitchen, Bedroom, InputValidation

#use for main room

def slow_print(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)

class MainRoom():

    def __init__(self,study_key,safe_pin,contract,bottle):
        print("================================ Welcome to the game ================================\n")
        print("Type the numbers displayed onscreen in order to make your choice\n")
        self.intro = "You are the friend of affluent industrialist Issac Hobbes and have been invited to his estate for a formal dinner to celebrate his engagement to Janet Hawthorne.\n\nThere are four other guests at this dinner: \n   - His son, William Hobbes \n   - His business partner, Tareth Codwen \n   - His daughter, Mia Hobbes\n   - His brother, Andrew Hobbes\nThe night is going well. You all sit around the grand dining room table as the dinner is being served. However, as Issac stands to make a toast to his fiance, he takes a sip of his wine and suddently starts to spit blood. You all watch as he convulses on the floor, spitting blood. Within moments, he is dead, and it is up to you to figure out who did it."
        slow_print(self.intro)
        self.main_room(study_key,safe_pin,contract,bottle)

    def main_room(self,study_key,safe_pin,contract,bottle):
        prompt = """
You are in the dining room -what would you like to do?
    1 - Talk to William
    2 - Talk to Tareth
    3 - Talk to Mia
    4 - Talk to Andrew
    5 - Talk to Janet
    6 - Head out to the hallway\n"""
        slow_print(prompt)
        choice = InputValidation.check6()
        if choice == "1":
            #william()
            print("PLACE")
        elif choice == "2":
            Tareth.Tareth(contract, bottle)
        elif choice == "3":
            #mia()
            print("PLACE")
        elif choice == "4":
            #andrew()
            print("PLACE")
        elif choice == "5":
            #janet(safe_pin)
            print("PLACE")
        else:
            #self.hallway()
            print("PLACE")

    def hallway(self):
        prompt = """
    You are now in the hallway - where would you like to go?
        1 - The kitchen
        2 - The Study
        3 - The Bedroom
        4 - Go Back\n"""
        slow_print(prompt)
        choice = InputValidation.check4()
        if self.choice == "1":
            kitchen()
        elif self.choice == "2":
            study()
        elif self.choice == "3":
            bedroom()
        else:
            self.main_room()

study_key = 0
safe_pin = 0
contract = 0
bottle = 0
MainRoom(study_key, safe_pin, contract, bottle)