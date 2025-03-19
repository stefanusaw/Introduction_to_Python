class Inventory():
    def __init__(self):
        self.inventory = {"apple": (10, 2.5), "banana": (20, 1.2)}

    def add(self, item, quantity, price):
        self.inventory[item] = (quantity, price)
    
    def remove(self, item):
        if item in self.inventory:
            del self.inventory[item]
            print(f"Removed {item} from inventory.")
        else:
            print(f"{item} not found in inventory.")
        
    def update(self, item, quantity=None, price=None):
        current_quantity, current_price = self.inventory[item]
        if quantity is not None:
            current_quantity = quantity
        if price is not None:
            current_price = price
        self.inventory[item] = (current_quantity, current_price)
        print(f"Updated inventory = {self.inventory}")
        
    def display(self):
        for item, (quantity, price) in self.inventory.items():
            print(f"Item: {item}, Quantity = {quantity}, Price = ${price}")
    
    def getTotalValue(self):
        tot = 0
        for (quantity, price) in self.inventory.values():
            tot += quantity * price
        print(f"Total value of inventory: ${tot}")
        
        
inv = Inventory()

inv.add("mango", 15, 3.0)
inv.update("apple", 12, 2.8)
inv.remove("banana")

inv.display()
inv.getTotalValue()