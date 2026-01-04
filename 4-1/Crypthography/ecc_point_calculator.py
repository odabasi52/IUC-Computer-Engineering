"""
Eliptic Curve Parameters
"""

p = 383
a = 5
b = 7
k = 50
starting_point = (2, 5)


def modular_inverse(x: int, y: int):
    if x == 0:
        return 0
    if y == 0:
        return 0

    a, b = x, y
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    while b != 0:
        q = a // b
        r = a % b
        s = s1 - q * s2
        t = t1 - q * t2

        a, b = b, r
        s1, s2 = s2, s
        t1, t2 = t2, t

    return s1

def is_point_on_curve(a, b):
    val = (((pow(a, 3)* 4) % p) + ((27 * b) % p)) % p
    return val != 0

def calculate_point(k: int):
    if not is_point_on_curve(a, b):
        raise ValueError("The given a and b do not define a valid elliptic curve.")
    else:
        print(f"y^2 = x^3 + {a}x + {b}  (mod {p}) is a valid elliptic curve.\n")

    binary_k = bin(k)[3:]
    x1, y1 = starting_point
    starting_x, starting_y = starting_point
    P = 1
    print(f"\t1P = ({x1}, {y1})")
    for i in binary_k:
        L_double = ((3 * pow(x1, 2) + a) % p) * modular_inverse(2 * y1, p) % p
        x3 = (pow(L_double, 2) - 2 * x1) % p
        y3 = (L_double * (x1 - x3) - y1) % p
        print(f"\t{P}P + {P}P = {2*P}P \t\t({x3}, {y3})")
        P *= 2
        if i == '1':
            L_add = (y3 - starting_y) * modular_inverse((x3 - starting_x) % p, p) % p
            x4 = (pow(L_add, 2) - x3 - starting_x) % p
            y4 = (L_add * (x3 - x4) - y3) % p
            print(f"\t{P}P + 1P = {P+1}P \t\t({x4}, {y4})")
            P += 1
            x1, y1 = x4, y4
        else:
            x1, y1 = x3, y3
    return (x1, y1)

if __name__ == "__main__":
    point = calculate_point(k)
    if point:
        print(f"\t\nThe point {k}P is: {point}")
    else:
        print(f"\t\nThe point {k}P is the point at infinity.")