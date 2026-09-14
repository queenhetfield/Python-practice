"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`."""
    return tuple((dish_name, set(dish_ingredients)))

def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`."""
    if ALCOHOLS.isdisjoint(drink_ingredients):
        return f"{drink_name} Mocktail"
    return f"{drink_name} Cocktail"

def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`."""
    diets = {"VEGAN": VEGAN, "VEGETARIAN": VEGETARIAN, "PALEO": PALEO, "KETO": KETO, "OMNIVORE": OMNIVORE}
    for name, ingredients in diets.items():
        if dish_ingredients.issubset(ingredients):
            return f"{dish_name}: {name}"
    return None
            
def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`."""
    special_ings = set(dish[1]).intersection(SPECIAL_INGREDIENTS)
    return tuple((dish[0], special_ings))
    
def compile_ingredients(dishes):
    """Create a master list of ingredients."""
    all_dishes = set()
    for dish in dishes:
        all_dishes.update(dish)
    return all_dishes

def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them."""
    return list(set(dishes).difference(set(appetizers)))

def singleton_ingredients(dishes, intersection):
    """Find singleton ingredients within the group of dishes (ingredients that only appear once across dishes)."""
    singletons = set()
    for dish in dishes:
        difference = dish.symmetric_difference(intersection)
        singletons.update(difference)
    singletons.difference_update(intersection)
    return singletons
