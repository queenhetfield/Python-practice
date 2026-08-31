"""Given a positive integer, return the number of steps
it takes to reach 1 according to the rules of the Collatz Conjecture."""
def steps(number):
    count = 0
    while number != 1:
        if number <= 0:
            raise ValueError("Only positive integers are allowed")
        if (number % 2) == 0:
            number = number / 2
        elif (number % 2) != 2:
            number = number * 3 + 1
        elif number == 1:
            print (0)
        count += 1
    return count
