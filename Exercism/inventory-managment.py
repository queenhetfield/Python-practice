"""Functions to keep track and alter inventory."""

def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list."""
    items_set = set(items)
    items_dict = {}
    for item in items_set:
        items_dict[item] = items.count(item)
    return items_dict

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`."""
    items_dict = create_inventory(items)
    original_dict = inventory.copy()
    for key, item in items_dict.items():
        if key in original_dict:
            original_dict[key] = original_dict[key] + item
        else:
            original_dict[key] = item
    return original_dict
    
def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list."""
    items_dict = create_inventory(items)
    original_dict = inventory.copy()
    for key, item in items_dict.items():
        if key in original_dict:
            original_dict[key] = original_dict[key] - item
            if original_dict[key] < 0:
                original_dict[key] = 0
    return original_dict

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string."""
    if item in inventory:
        inventory.pop(item)
    return inventory

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory."""
    original_dict = inventory.copy()
    for key, item in inventory.items():
        if item == 0:
            original_dict.pop(key)
    return list(original_dict.items())
