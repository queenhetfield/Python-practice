"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart."""
    for item in items_to_add:
        current_cart.setdefault(item, 0)
        current_cart[item] += 1
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry."""
    return dict.fromkeys(notes, 1)

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary."""
    ideas |= recipe_updates
    return ideas
    

def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order."""
    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart

def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information."""
    sorted_cart = dict(sorted(cart.items(), reverse=True))
    for name, count in sorted_cart.items():
        sorted_cart[name] = [count, *aisle_mapping[name]]
    return sorted_cart
        

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order."""

