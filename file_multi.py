import math

with open('input.txt') as f:
    for line in f:
        try:
            a, b, c = map(float, line.split())
            D = b**2 - 4*a*c
            x1 = (-b + math.sqrt(D)) / (2*a)
            x2 = (-b - math.sqrt(D)) / (2*a)
            print(x1, x2)
        except:
            print("Invalid input, skipped.")
