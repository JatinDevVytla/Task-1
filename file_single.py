import math
try:
    with open('input.txt') as f:
        a, b, c = map(float, f.readline().split())
    D = b**2 - 4*a*c
    if D >= 0:
        print(f"Roots: {(-b + math.sqrt(D)) / (2*a):.2f}, {(-b - math.sqrt(D)) / (2*a):.2f}")
    else:
        real = -b / (2*a)
        imag = math.sqrt(-D) / (2*a)
        print(f"Complex Roots: {real:.2f} ± {imag:.2f}i")
except:
    print("Invalid input")
