def euclid_find_gcd(x: int, y: int):
    if x == y:
        return x
    elif (x == 0 and y != 0):
        return y
    elif (y == 0 and x != 0):
        return x

    if x > y:
        a = x
        b = y
    else:
        a = y
        b = x

    while (True):
        c = a % b
        if c == 0:
            break
        a = b
        b = c
    return b

def euclid_find_constants(x: int, y: int):
    if x == 0:
        return f"{y} = 1.{y}" 
    if y == 0:
        return f"{x} = 1.{x}" 

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

    return f"{a} = {x}.{s1} + {y}.{t1}" 

print(euclid_find_constants(70, 110))