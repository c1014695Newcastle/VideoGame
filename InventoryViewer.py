import sys, time


def slow_print(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.025)


class InventoryViewer:

    def __init__(self, inventory):
        if all(i == 0 for i in inventory):
            slow_print("You have nothing in your inventory to view")
            return
        else:
            self.filtered_list = filter(lambda item: item[1] == 1, inventory)
            print(self.filtered_list)
            for x, item in enumerate(self.filtered_list):
                print(item, " - ", self.filtered_list[x])

    def view_item(self):
        item_choice = "hi"


inventory = {"Study Key": 1, "Safe Pin": 1, "Contract": 0, "Scotch Bottle": 0, "Wine Bottle": 1,
             "Password": 0}
InventoryViewer(inventory)