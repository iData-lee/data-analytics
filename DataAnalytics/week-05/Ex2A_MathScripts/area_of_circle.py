# To calculate the area of a circle you would need to mulitply pi by the square of the radius
#  The radius is half of a circles diameter.
import math
diameter = 18 
radius = diameter // 2
area = math.pi * radius**2

print(f'The area of a circle with radius {radius} is {area:.2f}')