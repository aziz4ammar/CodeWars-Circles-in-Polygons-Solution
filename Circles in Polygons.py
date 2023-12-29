import math

def circle_diameter(sides, side_length):
    apothem = side_length / (2 * math.tan(math.pi / sides))
    diameter = 2 * apothem
    return diameter

def in_circle(sides, side_length):
    radius = circle_diameter(sides, side_length) / 2
    area = math.pi * radius**2
    return area