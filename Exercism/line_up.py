"""Module providing a function to generate tickets."""
def line_up(name, number):
    """Function returning full sentence with name and corrent number ending."""
    special_numbers = [11, 12, 13]
    endings = {1: "st", 2: "nd", 3: "rd"}
    ending = "th"
    for key, value in endings.items():
        if number % 100 not in special_numbers and number % 10 == key:
            ending = value
            break
    return f"{name}, you are the {number}{ending} customer we serve today. Thank you!"
