"""Functions to automate Conda airlines ticketing system."""

seats = ["A", "B", "C", "D"]
def generate_seat_letters(number):
    """Generate a series of letters for airline seats."""
    index = 0
    while index < number:
        yield seats[index%4]
        index += 1

def generate_seats(number):
    """Generate a series of identifiers for airline seats."""
    index = 0
    while index < number:
        row = index // len(seats) + 1
        if row >= 13:
            row += 1
        yield f"{row}{seats[index % len(seats)]}"
        index += 1

def assign_seats(passengers):
    """Assign seats to passengers."""
    assigned = {}
    seat = generate_seats(len(passengers))
    for name in passengers:
        assigned[name] = next(seat)
    return assigned

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket."""
    for seat in seat_numbers:
        zeros = 12 - len(seat) - len(flight_id)
        yield f"{seat}{flight_id}{zeros * "0"}"
        