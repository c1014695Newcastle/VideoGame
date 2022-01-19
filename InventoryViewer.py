import sys, time


def slow_print(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.025)


class InventoryViewer:

    def __init__(self, inventory):
        if all(i == 0 for i in inventory):
            print("1 - Notepad")
            return
        else:
            print("Your inventory items are:\n\t 1 - Notepad")
            filtered_list = {}
            n = 2
            for x in inventory:
                if inventory[x] == 1:
                    filtered_list[n] = x
                    print("\t", n, "-", filtered_list[n]) # expected output e.g: 1 - Study Key

                    n = n + 1

    def view_item(self):
        item_choice = "hi"


#inventory = {"Study Key": 1, "Safe Pin": 1, "Contract": 0, "Scotch Bottle": 0, "Wine Bottle": 1,
            # "Password": 0}
inventory = {"Study Key": 1, "Safe Pin": 0, "Contract": 1, "Scotch Bottle": 0, "Wine Bottle": 0, "Password": 0}

InventoryViewer(inventory)