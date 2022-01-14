

class InventoryViewer:

    def __init__(self, inventory):
        if all(i == 0 for i in inventory):
            slow_print("You have nothing in your inventory to view")
            return
        else:
            print("test")

    def view_item(self):
        print("PLACE")
