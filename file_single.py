import math
a, b, c = map(float, open('input.txt').readline().split())
D = b**2 - 4*a*c
if D >= 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Roots: {x1:.2f}, {x2:.2f}")
else:
    real = -b / (2*a)
    imag = math.sqrt(-D) / (2*a)
    print(f"Complex Roots: {real:.2f} ± {imag:.2f}i")
