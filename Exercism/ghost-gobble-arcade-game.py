"""Functions for implementing the rules of the classic arcade game Pac-Man."""
def eat_ghost(power_pellet_active, touching_ghost):
    eat = power_pellet_active and touching_ghost
    return eat
def score(touching_power_pellet, touching_dot):
    scr = touching_power_pellet or touching_dot
    return scr
def lose(power_pellet_active, touching_ghost):
    lost = not power_pellet_active and touching_ghost
    return lost
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Function to check if Pac-Man wins"""
    main_cond = has_eaten_all_dots
    cond_1 = power_pellet_active and touching_ghost
    cond_2 = not touching_ghost
    winner = main_cond and (cond_1 or cond_2)
    return winner
