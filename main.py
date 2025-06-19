
def main():
    print("Welcome to the Inventory Management System")
    # Initialize inventory service and other components here
    # Handle user interactions (e.g., menu options, input handling)

if __name__ == "__main__":


    class Inventory:
        def __init__(self):
            self.items = {}

        def add_item(self, name, quantity):
            if name in self.items:
                self.items[name] += quantity
            else:
                self.items[name] = quantity

        def remove_item(self, name, quantity):
            if name in self.items:
                if self.items[name] >= quantity:
                    self.items[name] -= quantity
                    if self.items[name] == 0:
                        del self.items[name]
                    return True
                else:
                    print("Not enough quantity to remove.")
            else:
                print("Item not found.")
            return False

        def display_inventory(self):
            if not self.items:
                print("Inventory is empty.")
            else:
                print("Current Inventory:")
                for name, quantity in self.items.items():
                    print(f"{name}: {quantity}")

    def main():
        inventory = Inventory()
        while True:
            print("\nMenu:")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. Display Inventory")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                name = input("Enter item name: ")
                try:
                    quantity = int(input("Enter quantity: "))
                    inventory.add_item(name, quantity)
                    print("Item added.")
                except ValueError:
                    print("Invalid quantity.")
            elif choice == "2":
                name = input("Enter item name: ")
                try:
                    quantity = int(input("Enter quantity to remove: "))
                    if inventory.remove_item(name, quantity):
                        print("Item removed.")
                except ValueError:
                    print("Invalid quantity.")
            elif choice == "3":
                inventory.display_inventory()
            elif choice == "4":
                print("Exiting Inventory Management System.")
                break
            else:
                print("Invalid choice. Please try again.")

    if __name__ == "__main__":
        main()
