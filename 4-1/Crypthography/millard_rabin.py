import sys 
from random import randint 

def millard_rabin_m_k_extractor(n):
    k = 0
    while n % 2 == 0:
        n = n // 2
        k += 1
    m = n
    return m, k

def millard_rabin_probability_test(n, iterations):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    m, k = millard_rabin_m_k_extractor(n - 1)
    is_prime = False
    for _ in range(iterations):
        is_prime = False
        a = randint(2, n - 1)
        b = pow(a, m, n)
        if b == 1 or b == n - 1:
            is_prime = True
            continue
        for _ in range(k):
            b = pow(b, 2, n)
            if b == n - 1:
                is_prime = True
                break
        if not is_prime:
            return False
    return True

if __name__ == "__main__":
    try:
        assert len(sys.argv) == 3
    except:
        print("Usage: python millard_rabin.py <number> <iterations>")
        sys.exit(1)
    
    n = int(sys.argv[1])
    iterations = int(sys.argv[2])
    if millard_rabin_probability_test(n, iterations):
        print(f"{n} is probably prime")
    else:
        print(f"{n} is composite")

"""
Examples:
└─$ python millard_rabin.py 171860471149189498224797041015852353811297365192058311872168073014541823242841534570844847030144038948199605814576374674573049794357093945782451900951812579895331107930680276330224230748216892296906706376860527299833890067633046394755300880528858839985558194677133129035986723998136712299883353099629736872121 100                                          
171860471149189498224797041015852353811297365192058311872168073014541823242841534570844847030144038948199605814576374674573049794357093945782451900951812579895331107930680276330224230748216892296906706376860527299833890067633046394755300880528858839985558194677133129035986723998136712299883353099629736872121 is probably prime

└─$ python millard_rabin.py 25 24
25 is composite
"""
