from main import slow_print, hallway
import ReusedCode


class StudyRoom:

    def __init__(self, inventory):
        slow_print("""
You are in Issac's Study room, what would you like to do?
    1 - Check the desk
    2 - Check the cupboard
    3 - Check the bookshelf
    4 - Check the cabinet
    5 - LEAVE""")
        self.choice = InputValidation.check5()
        if self.choice == "1":
            self.desk(inventory)
        elif self.choice == "2":
            self.cupboard(inventory)
        elif self.choice == "3":
            self.bookshelf(inventory)
        elif self.choice == "4":
            self.cabinet(inventory)
        else:
            return

    def desk(self, inventory):
        slow_print("""
You are at Issac's desk, what would you like to check?
    1 - Drawers
    2 - Computer
    3 - Go back to the main room""")
        choice = InputValidation.check3()
        if choice == "1":
            slow_print("""
You find the standard stuff: a loose bunch of pens, some sticky notes and a notebook. There's nothing to help you find the murderer.""")
            self.desk(inventory)
        elif choice == "2":
            self.computer(inventory)
        else:
            exit()

    def computer(self, inventory):
        password = "dMhpYyQUKsFj"
        if inventory["Password"] == 0:
            slow_print("""
The computer is protected by a password, you must be able to find it somewhere. You can still try and guess""")
        else:
            slow_print(f"HINT: The password to his computer is {password}")
        password_guess = input("PASSWORD: ")
        if password_guess == password:
            print("Access granted")
            # COMPUTER FILE ACCESS
        else:
            print("Access denied")
            slow_print("Would you like to try again?\n  1 - Yes\n   2 - No")
            choice = InputValidation.check2()
            if choice == "1":
                self.computer(inventory)
