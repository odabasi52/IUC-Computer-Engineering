def fast_modular_exponential(a, b, m):
    """
        a^b (mod m)
    """
    b = bin(b)[2:] 
    c = 0
    d = 1
    for i in b:
        c = (c * 2) % m
        d = (d * d) % m
        if i == '1':
            c = (c + 1) % m
            d = (d * a) % m
    return d

print(fast_modular_exponential(7, 560, 561))