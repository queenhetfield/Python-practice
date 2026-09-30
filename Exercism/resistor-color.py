"""Module, that contains functions which tell color number, lists all colors,
returns first two bands value and label."""
color_numbers = {"black":0 ,"brown": 1, "red": 2, "orange": 3, "yellow": 4,
                 "green": 5, "blue": 6, "violet": 7, "grey": 8, "white":9}
def color_code(color):
    """Function to tell color number."""
    return color_numbers[color]
def colors():
    """Function to list all colors."""
    return list(color_numbers)
def value(colors):
    """Fuction returning first two bands value."""
    return color_numbers[colors[0]] * 10 + color_numbers[colors[1]]
def label(colors):
    """Function returning resistance label."""
    numeric = value(colors) * 10 ** color_numbers[colors[2]]
    if numeric == 0:
        return f"{numeric} ohms"
    if numeric % (10 ** 9) == 0:
        return f"{numeric // (10 ** 9)} gigaohms"
    if numeric % (10 ** 6) == 0:
        return f"{numeric // (10 ** 6)} megaohms"
    if numeric % (10 ** 3) == 0:
        return f"{numeric // (10 ** 3)} kiloohms"
    return f"{numeric} ohms"
def resistor_label(colors):
    """Function returning tolerance."""
    tolerance = {"grey": "±0.05%", "violet": "±0.1%", "blue": "±0.25%", "green": "±0.5%",
                 "brown": "±1%", "red": "±2%", "gold": "±5%", "silver": "±10%"}
    if len(colors) == 5:
        numeric = (value(colors) * 10 + color_numbers[colors[2]]) * 10 ** color_numbers[colors[3]]
        if numeric / (10 ** 9) > 1:
            numeric = f"{numeric / (10 ** 9)} gigaohms"
        elif numeric / (10 ** 6) > 1:
            numeric = f"{numeric / (10 ** 6)} megaohms"
        elif numeric / (10 ** 3) > 1:
            numeric = f"{numeric / (10 ** 3)} kiloohms"
        return f"{numeric} {tolerance[colors[4]]}"
    if len(colors) == 4:
        return f"{label(colors)} {tolerance[colors[3]]}"
    return label(colors)

print(resistor_label(["violet", "orange", "red", "grey"]))
