"""Functions to keep track and alter inventory."""

def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list."""
    item_dict = {}
    for item in items:
        item_dict.setdefault(item, 0)
        item_dict[item] += 1
    return item_dict

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`."""
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory
    
def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list."""
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string."""
    if item in inventory:
        inventory.pop(item)
    return inventory

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory."""
    available_items = {
        name: count
        for name, count in inventory.items()
        if count > 0
    }
    return list(available_items.items())