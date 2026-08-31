"""Module providing a functions to identify triangles."""
def equilateral(sides):
    if len(set(sides)) == 1:
        return triangle(sides)
    return False
def isosceles(sides):
    if len(set(sides)) == 2 or len(set(sides)) == 1:
        return triangle(sides)
    return False
        
def scalene(sides):
    if len(set(sides)) == 3:
        return triangle(sides)
    return False
        
def triangle(sides):
    sort = sorted(sides)
    return sort[0] > 0 and sort[2] < sum(sort[:2])
