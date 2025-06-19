class InventoryService:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.id in self.items:
            raise ValueError("Item with this ID already exists.")
        self.items[item.id] = item

    def remove_item(self, item_id):
        if item_id not in self.items:
            raise ValueError("Item not found.")
        del self.items[item_id]

    def get_item(self, item_id):
        return self.items.get(item_id, None)

    def list_items(self):
        return list(self.items.values())