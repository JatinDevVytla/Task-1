import math

with open('input.txt') as f:
    for line in f:
        try:
            a, b, c = map(float, line.split())
            D = b**2 - 4*a*c
            x = lambda s: (-b + s * math.sqrt(abs(D))) / (2*a)
            result = f"{x(1):.2f}, {x(-1):.2f}"
            print(f"{'Roots' if D >= 0 else 'Complex'}: {result}{'' if D >= 0 else 'i'}")
        except:
            print("Invalid input")
