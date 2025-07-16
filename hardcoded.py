import math
a, b, c = 1, -3, 2
D = b**2 - 4*a*c
x = lambda s: (-b + s * math.sqrt(abs(D))) / (2*a)
print(f"{'Roots' if D >= 0 else 'Complex'}: {x(1):.2f}, {x(-1):.2f}{'' if D >= 0 else 'i'}")
