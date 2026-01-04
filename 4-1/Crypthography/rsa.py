"""
Private Values
"""
p = 885320963
q = 238855417
a = 116402471153538991


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

def generate_public_key():
    n = p * q 
    fi = (p - 1) * (q - 1)
    b = modular_inverse(a, fi) % (fi)
    return n, b

def encrypt_message(n, b, x: int):
    y = pow(x, b, n) 
    return y

def decrypt_message(n, y: int):
    x = pow(y, a, n)
    return x


def encrypt_text(n, b, x: str):
    encrypted_chars = []
    for char in x:
        ascii_val = ord(char)
        y = encrypt_message(n, b, ascii_val)
        encrypted_chars.append(y)
    return encrypted_chars

def decrypt_text(n, encrypted_chars: list):
    decrypted_text = ""
    for y in encrypted_chars:
        ascii_val = decrypt_message(n, y)
        decrypted_text += chr(ascii_val)
    return decrypted_text

import sys
if __name__ == "__main__":
    if len(sys.argv) != 2:
       print("Usage: python rsa.py <message_integer>")
       print("Usage: python rsa.py <ascii_text>")
       sys.exit(1)
    if not sys.argv[1].isdigit():
        text = sys.argv[1]
        n, b = generate_public_key()
        print(f"Public Values: (n={n}, b={b})")
        print(f"Private Values a: {a}, p: {p}, q: {q}")

        encrypted_text = encrypt_text(n, b, text)
        print(f"Encrypted Text: {encrypted_text}")

        decrypted_text = decrypt_text(n, encrypted_text)
        print(f"Decrypted Text: {decrypted_text}")
    else:
        message = int(sys.argv[1])
        n, b = generate_public_key()
        print(f"Public Values: (n={n}, b={b})")
        print(f"Private Values a: {a}, p: {p}, q: {q}")

        encrypted_message = encrypt_message(n, b, message)
        print(f"Encrypted Message: {encrypted_message}")

        decrypted_message = decrypt_message(n, encrypted_message)
        print(f"Decrypted Message: {decrypted_message}")


