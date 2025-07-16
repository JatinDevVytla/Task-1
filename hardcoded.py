import math
a, b, c = 1, -3, 2
D = b**2 - 4*a*c
print((-b + math.sqrt(D)) / (2*a), (-b - math.sqrt(D)) / (2*a))
