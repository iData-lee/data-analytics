# The distance between two points comes from the Pythagorean Theorem

import math 

x1, y1 = 1, 2
x2, y2 = 8, 9

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}.")
