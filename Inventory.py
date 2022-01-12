from main import slow_print

class InventoryViewer:

    def __init__(self, inventory):
        if all(i == 0 for i in inventory):
            slow_print("You have nothing in your inventory to view")
            return
        else:
            self.filtered_list = list(filter(x == 1 for x in inventory))
            print(self.filtered_list)

    def view_item(self):
        print("PLACE")

InventoryViewer()
