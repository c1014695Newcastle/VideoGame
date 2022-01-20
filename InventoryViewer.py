import sys, time

import InputValidation


def slow_print(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.025)


class InventoryViewer:

    def __init__(self, inventory):
        print("================================ INVENTORY ================================\n")
        if all(i == 0 for i in inventory):
            print("HERE")
        else:
            print("Your inventory items are:")
            filtered_list = {}
            filtered_list[1] = "Notepad"
            n = 2
            for x in inventory:
                if inventory[x] == 1:
                    filtered_list[n] = x
                     # expected output e.g: 1 - Study Key

                    n = n + 1
            filtered_list[n+1]= "Return to game"
            self.view_item(n, filtered_list, inventory)

    def item_picker(self, item, inventory):
        for w in inventory:
            if item == w:
                if w == "Safe Pin":
                    text = self.safe_pin_view()
                elif w == "Study Key":
                    text = self.study_key_view()
                elif w == "Contract":
                    text = self.contract_view()
                elif w == "Scotch Bottle":
                    text = self.scotch_bottle_view(inventory)
                elif w == "Wine Bottle":
                    text = self.wine_bottle_view(inventory)
                elif w == "Poison":
                    text = self.poison_view(inventory)
        slow_print(text)

    def view_item(self, n, filtered_list, inventory):
        choice = ""
        while choice != str(n):
            for u in filtered_list:
                print("\t", u, "-", filtered_list[u])
            choice = InputValidation.checkn(n)
            if choice == "1":
                print("Place")
                # Notepad.Notepad(progress_monitor)
            else:
                for w in range(2,len(filtered_list) + 1):
                    for y in filtered_list:
                        if y == w:
                            self.item_picker(filtered_list[w], inventory)

    def study_key_view(self):
        text = "The key to Issac's Study"
        return text

    def safe_pin_view(self):
        text = """
The pin to Issac's Bedroom Safe, written on a napkin. The only other person who he told this was Janet."""
        return text

    def contract_view(self):
        print("==== ISSAC'S CONTRACT ====\n")
        text = """
A shady business contract between Tareth and Issac's firm and a larger competitor. The contract had several cuts to employee benefits in order to increase profit margins. Tareth agreed to the terms, however, Issac refused to sign his name. Thus the deal never occurred. But why would be keep it?"""
        return text

    def scotch_bottle_view(self, inventory):
        if inventory["Poison Bottle"] == 1:
            text = """
A bottle of Issac's favourite scotch and a gift from his old business partner in a bid to bring them back to work. Issac never drank it. It has a strange odour to it that you can't recognise as any added flavourings."""
        else:
            text = """
A bottle of Issac's favourite scotch and a gift from his old business partner in a bid to bring them back to work. Issac never drank it."""
        return text

    def wine_bottle_view(self, inventory):
        if inventory["Poison Bottle"] == 1:
            text = """
The bottle of wine that killed Issac. Everybody else at the table drank it, and it has no smell of poison, so the killer must have put the poison in the glass before he made the toast..."""
        else:
            text = """The wine bottle from the table."""
        return text

    def poison_view(self, inventory):
        if inventory["Scotch Bottle"] == 1 and inventory["Wine Bottle"] == 1:
            text = """
The bottle of poison that killed Issac. The killer must have slipped it in the glass, since bottle has no poison smell. It has an odd smell, similar but not exactly the same as the scotch bottle."""
        elif inventory["Scotch Bottle"] == 0 and inventory["Wine Bottle"] == 1:
            text = """
The bottle of poison that killed Issac. The killer must have slipped it in the glass, since bottle has no poison smell."""
        elif inventory["Scotch Bottle"] == 1 and inventory["Wine Bottle"] == 0:
            text = """
The bottle of poison that killed Issac. It has an odd smell, similar but not exactly the same as the scotch bottle."""
        else:
            text = "The bottle of poison that killed Issac"
        return text

progress_monitor = {}
#inventory = {"Study Key": 1, "Safe Pin": 1, "Contract": 0, "Scotch Bottle": 0, "Wine Bottle": 1,
            # "Password": 0}
inventory = {"Study Key": 1,"Poison": 0, "Safe Pin": 0, "Contract": 1, "Scotch Bottle": 0, "Wine Bottle": 0, "Password": 0}

InventoryViewer(inventory)