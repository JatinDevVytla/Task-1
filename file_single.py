import math
with open('input.txt') as f:
    a, b, c = map(float, f.readline().split())
    D = b**2 - 4*a*c
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(x1, x2)
