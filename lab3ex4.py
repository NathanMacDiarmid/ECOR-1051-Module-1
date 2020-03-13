import math


def area_of_cone(height, radius):
    x = math.sqrt(radius**2 + height**2)
    y = math.pi * radius
    return x * y


print(area_of_cone(5, 2))
print(area_of_cone(0, 2))
print(area_of_cone(5, 0))
