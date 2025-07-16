import math
a, b, c = map(float, open('input.txt').readline().split())
D = b**2 - 4*a*c
if D >= 0:
    print((-b + math.sqrt(D)) / (2*a), (-b - math.sqrt(D)) / (2*a))
else:
    print("Complex roots")
