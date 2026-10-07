"""Module providing functions to calculate different
    squared values of fisrt N natural numbers."""
def square_of_sum(number):
    """Function returning square of the sum of fisrt N natural numbers."""
    return sum(num for num in range(number + 1)) ** 2

def sum_of_squares(number):
    """Function returning sum of the squares of fisrt N natural numbers."""
    return sum(num ** 2 for num in range(number + 1))

def difference_of_squares(number):
    """Function returning the difference between the square of the sum
    of the first N natural numbers and the sum
    of the squares of the first N natural numbers."""
    return square_of_sum(number) - sum_of_squares(number)
