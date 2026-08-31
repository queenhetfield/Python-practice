"""Module providing a function checking if number is an Armstrong number"""
def is_armstrong_number(number):
    """Function checking if number is an Armstrong number"""
    digits = []
    num = number
    while num > 0:
        digit = num % 10
        digits.append(digit)
        num //= 10
    powers = []
    for digit in digits:
        power = digit ** len(digits)
        powers.append(power)
    
    return sum(powers) == number
    