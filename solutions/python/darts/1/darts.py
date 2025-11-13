import math

def distance_from_center(x, y):
    """
    Calculate distance from center (0, 0) to point (x, y).
    
    Returns:
        Distance as a float
    """
    # Apply Pythagorean theorem from origin (0, 0)
    return math.sqrt(x ** 2 + y ** 2)

def score(x, y):
    """
    Calculate dart score based on distance from center.
    
    Args:
        x: X coordinate of dart landing position
        y: Y coordinate of dart landing position
    
    Returns:
        Score as integer (0, 1, 5, or 10)
    """
    # Calculate distance from dartboard center (0, 0)
    point_distance = distance_from_center(x, y)
    
    # Outside target (radius > 10)
    if point_distance > 10:
        return 0
    # Outer circle (5 < radius <= 10)
    if point_distance > 5 and point_distance <= 10:
        return 1
    # Middle circle (1 < radius <= 5)
    if point_distance > 1 and point_distance <= 5:
        return 5
    # Inner circle (radius <= 1)
    if point_distance >= 0 and point_distance <= 1:
        return 10