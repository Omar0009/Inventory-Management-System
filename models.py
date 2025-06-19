class Item:
    def __init__(self, item_id, name, quantity, price):
        self.id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount):
        self.quantity += amount

    def get_details(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }