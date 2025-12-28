def jacobi_solver(a, n):
    if n % 2 == 0: 
        return 0 
    
    if a == 0: return 0
    if a == 1: return 1

    jacobi = 1
    a = a % n
    if a == 0: return 0
    while not (a == 1):
        while a % 2 == 0:
            a = a // 2
            if n % 8 == 3 or n % 8 == 5:
                jacobi *= -1
        if a == 1: break
        a, n = n, a 
        if a % 4 == 3 and n % 4 == 3:
            jacobi *= -1
        a = a % n
        if a == 0: return 0
    return jacobi

import random
def euler_solver(a, n):
    return pow(a, (n - 1) // 2, n)

def solovay_strassen_probability_test(n, k):
    if n == 2 or n == 3: return True
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = euler_solver(a, n)
        j = jacobi_solver(a, n) % n
        if j == 0 or x != j:
            return False
    return True


import sys 
if __name__ == "__main__":
    try:
        assert len(sys.argv) == 3
    except:
        print("Usage: python solovay_strassen.py <number> <iterations>")
        sys.exit(1)
    
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    if solovay_strassen_probability_test(n, k):
        print(f"{n} is probably prime")
    else:
        print(f"{n} is composite")

"""
EXAMPLES:
└─$ python solovay_strassen.py 171860471149189498224797041015852353811297365192058311872168073014541823242841534570844847030144038948199605814576374674573049794357093945782451900951812579895331107930680276330224230748216892296906706376860527299833890067633046394755300880528858839985558194677133129035986723998136712299883353099629736872121 1000
171860471149189498224797041015852353811297365192058311872168073014541823242841534570844847030144038948199605814576374674573049794357093945782451900951812579895331107930680276330224230748216892296906706376860527299833890067633046394755300880528858839985558194677133129035986723998136712299883353099629736872121 is probably prime

└─$ python solovay_strassen.py 11 11
11 is probably prime
"""
