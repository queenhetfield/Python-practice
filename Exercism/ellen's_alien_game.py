"""Solution to Ellen's Alien Game exercise."""
class Alien:
    """Class representing a person"""
    total_aliens_created = 0
    
    """Create an Alien object with location x_coordinate and y_coordinate."""
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1
        
    def hit(self):
        if self.health > 0:
            self.health -= 1
    def is_alive(self):
        return self.health != 0
        
    def teleport(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, other_object):
        pass
    
def new_aliens_collection(positions):
    """Function to call Alien class with a list of coordinates"""
    alien_objects = []
    for position in positions:
        alien_objects.append(Alien(*position))
    return alien_objects
    