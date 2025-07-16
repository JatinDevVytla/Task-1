import math
try:
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    D = b**2 - 4*a*c
    if D >= 0:
        print(f"Roots: {(-b + math.sqrt(D)) / (2*a):.2f}, {(-b - math.sqrt(D)) / (2*a):.2f}")
    else:
        real = -b / (2*a)
        imag = math.sqrt(-D) / (2*a)
        print(f"Complex: {real:.2f} ± {imag:.2f}i")
except:
    print("Invalid input")
