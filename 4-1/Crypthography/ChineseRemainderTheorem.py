def euclid_find_constants(x: int, y: int):
    if x == 0:
        return y
    if y == 0:
        return x

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

def chinese_remainder_theorem(given_mods):
    a_list = []
    m_list = []
    final_mode = 1
    sum = 0
    for a, m in given_mods:
        a_list.append(a)
        m_list.append(m)
        final_mode *= m
    for i, _ in enumerate(m_list):
        M = 1
        for j, _ in enumerate(m_list):
            if not i == j:
                M = M * m_list[j]
        c = euclid_find_constants(M, m_list[i])
        y = c % m_list[i]
        sum += (y*a_list[i]*M)
    print(f"x = {sum % final_mode} (mod {final_mode})")


if __name__ == "__main__":
    given_mods = [
        (9, 13),  # x = 9 (mod 13)
        (8, 11),  # x = 8 (mod 11)
        (1, 7)    # x = 1 (mod 7)
    ]
    chinese_remainder_theorem(given_mods)