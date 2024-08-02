import math

def circle(rad):
    pi = math.pi
    area = pi*(rad**2)
    perimeter = 2*pi*rad
    return (area, perimeter)
    
a , p = circle(5)

print("Area - ", round(a, 2), "\nPerimeter - ", round(p, 2))
