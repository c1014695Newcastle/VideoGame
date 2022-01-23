#Get the computer passcode from her
import sys, time
import InputValidation
from colorama import Fore


def slow_print(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.00001)


class Janet:

    def __init__(self, inventory, progress):
        slow_print("""
Janet stands in the far corner of the dinning room, quietly sobbing while drinking from a half empty glass in her hands. 
For what was supposed to be her and Issac's big night, it has certainly went sour.
""")
        self.conversation_picker(inventory, progress)

    def conversation_picker(self, inventory, progress):
        if (inventory["Password"] == 0 and progress["Study Unlocked"] == 0) or (inventory["Password"] == 1 and progress["Study Unlocked"] == 1):
            self.standard_conversation(inventory)
        elif progress["Study Unlocked"] == 1:
            self.password_conversation(inventory)

    def standard_conversation(self, inventory):
        start = Fore.MAGENTA + "\n[JANET]: What do you want?\n   1 - Ask about relationship with Issac\n   2 - Ask about relationship with William\n   3 - Ask about relationship with Mia\n   4 - Ask about relationship with Tareth\n   5 - Leave\n"
        slow_print(start)
        choice = InputValidation.check5()
        if choice == "1":
            self.issac_rel(inventory)
        elif choice == "2":
            self.william_rel(inventory)
        elif choice == "3":
            self.mia_rel(inventory)
        elif choice == "4":
            self.tareth_rel(inventory)
        else:
            return inventory

    def password_conversation(self, inventory):
        start = Fore.RED + "[TARETH]: What do you want?\n   1 - Ask about relationship with Issac\n    2 - Ask about relationship with William\n   3 - Ask about relationship with Mia\n   4 - Ask about relationship with Janet\n   5 - Ask about the bottle\n   6 - Leave"
        slow_print(start)
        choice = InputValidation.check6()
        if choice == "1":
            self.issac_rel(inventory)
        elif choice == "2":
            self.william_rel(inventory)
        elif choice == "3":
            self.mia_rel(inventory)
        elif choice == "4":
            self.tareth_rel(inventory)
        elif choice == "5":
            self.password(inventory)

    def password(self, inventory):
        slow_print(Fore.YELLOW + """
[YOU]: I got into Issac's study, but his computer is locked with a password. I need to check his files. Do you know it?""" + Fore.MAGENTA + """\n\n[JANET]: Yes, he told me never to tell anyone, but I guess desperate times call for desperate measures. Here.""" + Fore.WHITE + "\nJANET TAKES A NAPKIN FROM HER POCKET AND WRITES THE PASSWORD USING HER LIPSTICK.\n")
        inventory["Password"] = 1

