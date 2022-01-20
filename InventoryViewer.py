import sys, time

import InputValidation


def slow_print(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.025)


class InventoryViewer:

    def __init__(self, inventory):
        if all(i == 0 for i in inventory):
            self.view_item()
        else:
            print("Your inventory items are:\n\t 1 - Notepad")
            filtered_list = {}
            filtered_list[1] = "Notepad"
            n = 2
            for x in inventory:
                if inventory[x] == 1:
                    filtered_list[n] = x
                    print("\t", n, "-", filtered_list[n]) # expected output e.g: 1 - Study Key

                    n = n + 1
            print("\t", n+1, "- Return to game")
            self.view_item(n, filtered_list)

    def item_picker(self, item):
        print("UP TO HERE")

    def view_item(self, n, filtered_list):
        choice = InputValidation.checkn(n)
        if choice == "1":
            print("Place")
            # Notepad.Notepad(progress_monitor)
        else:
            for w in range(2,len(filtered_list)):
                for y in filtered_list:
                    if y == w:
                        w = str(w)
                        self.item_picker(filtered_list[w])


progress_monitor = {}
#inventory = {"Study Key": 1, "Safe Pin": 1, "Contract": 0, "Scotch Bottle": 0, "Wine Bottle": 1,
            # "Password": 0}
inventory = {"Study Key": 1, "Safe Pin": 0, "Contract": 1, "Scotch Bottle": 0, "Wine Bottle": 0, "Password": 0}

InventoryViewer(inventory)