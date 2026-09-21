"""Module providing a function determining if positive number is either perfect, abundant or deficient."""
def classify(number):
    """ A perfect number equals the sum of its positive divisors."""
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    factors = [factor for factor in range(1, number) if number % factor == 0]
    if sum(factors) == number:
        return "perfect"
    if sum(factors) > number:
        return "abundant"
    if sum(factors) < number:
        return "deficient"
    
    return None