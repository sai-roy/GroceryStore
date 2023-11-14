class GroceryStore:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
        print(f"Added {quantity} {item}(s) to the inventory.")

    def update_quantity(self, item, new_quantity):
        if item in self.inventory:
            self.inventory[item] = new_quantity
            print(f"Updated {item} quantity to {new_quantity}.")
        else:
            print(f"{item} not found in the inventory.")

    def view_inventory(self):
        print("\nCurrent Inventory:")
        if not self.inventory:
            print("Inventory is empty.")
        else:
            for item, quantity in self.inventory.items():
                print(f"{item}: {quantity}")

    def remove_item(self, item):
        if item in self.inventory:
            del self.inventory[item]
            print(f"Removed {item} from the inventory.")
        else:
            print(f"{item} not found in the inventory.")

def main():
    grocery_store = GroceryStore()

    while True:
        print("\nOptions:")
        print("1. Add new item to inventory")
        print("2. Update item quantity")
        print("3. View inventory")
        print("4. Remove item from inventory")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            item = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            grocery_store.add_item(item, quantity)
        elif choice == "2":
            item = input("Enter the item name: ")
            new_quantity = int(input("Enter the new quantity: "))
            grocery_store.update_quantity(item, new_quantity)
        elif choice == "3":
            grocery_store.view_inventory()
        elif choice == "4":
            item = input("Enter the item name: ")
            grocery_store.remove_item(item)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()