import sys 
import random

"""
El-Gamal Cryptosystem Parameters
"""
p = 2579
alpha = random.randint(2, p - 2) 

"""
Private key  a
"""
a = 765

"""
Random integer k
"""
k = random.randint(2, p - 2)



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

def generate_public_key(alpha: int, a: int, p: int):
    beta = pow(alpha, a, p)
    return beta

def encrypt_message(beta: int, x: int):
    y1 = x * pow(beta, k, p) % p
    y2 = pow(alpha, k, p) # y2 = alpha^k mod p
    return (y1, y2)

def decrypt_message(y1: int, y2: int, a: int):
    x = pow(y1 * modular_inverse(pow(y2, a, p), p), 1, p) # x = y1 * (y2^a)^-1 mod p
    return x


def encrypt_text(text: str, beta: int):
    encrypted_chars = []
    for char in text:
        ascii_val = ord(char)
        y1, y2 = encrypt_message(beta, ascii_val)
        encrypted_chars.append((y1, y2))
    return encrypted_chars

def decrypt_text(encrypted_chars: list, a: int):
    decrypted_text = ""
    for y1, y2 in encrypted_chars:
        ascii_val = decrypt_message(y1, y2, a)
        decrypted_text += chr(ascii_val)
    return decrypted_text


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python el_gamal.py <message_integer>")
        print("Usage: python el_gamal.py <ascii_text>")
        sys.exit(1)
    
    if sys.argv[1].isdigit() == False:
        text_message = sys.argv[1]
        beta = generate_public_key(alpha, a, p)
        print(f"Public Key (p, alpha, beta): ({p}, {alpha}, {beta})")
        print(f"Private Key a: {a}")
        print(f"Random integer k: {k}")

        encrypted_chars = encrypt_text(text_message, beta)
        print(f"Encrypted Text: {encrypted_chars}")

        decrypted_text = decrypt_text(encrypted_chars, a)
        print(f"Decrypted Text: {decrypted_text}")
    else:
        message = int(sys.argv[1])

        beta = generate_public_key(alpha, a, p)
        print(f"Public Key (p, alpha, beta): ({p}, {alpha}, {beta})")
        print(f"Private Key a: {a}")
        print(f"Random integer k: {k}")

        y1, y2 = encrypt_message(beta, message)
        print(f"Encrypted Message (y1, y2): ({y1}, {y2})")

        decrypted_message = decrypt_message(y1, y2, a)
        print(f"Decrypted Message: {decrypted_message}")
