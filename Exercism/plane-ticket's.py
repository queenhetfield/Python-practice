"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats."""
    seats = ["A", "B", "C", "D"]
    index = 0
    while index < number:
        yield seats[index%4]
        index += 1

def generate_seats(number):
    """Generate a series of identifiers for airline seats."""
    


def assign_seats(passengers):
    """Assign seats to passengers."""



def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket."""
