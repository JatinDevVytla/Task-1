import math
a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4*a*c
print((-b + math.sqrt(D)) / (2*a), (-b - math.sqrt(D)) / (2*a))
