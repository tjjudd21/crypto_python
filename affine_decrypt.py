"""
To decipher an Affine cipher text, we must perform the inverse function on the ciphertext.

Function: D(x) = a^-1(x - b) mod m, where a^-1 is the modular multiplicative inverse of a modulo m.
i.e., it satisfies the equation 1 = a^-1 mod m
The easiest way to solve this problem is to search each of the numbers 1 to 25 and see which one satisfies the equation.
"""

# Elucidean algorithm for finding modular inverse
def egcd(a, b):
    x, y = 0, 1
    u, v = 1, 0

    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b,a, x,y, u,v, = a,r, u,v, m,n
    gcd = b

    return gcd, x, y

def modinv(a, m):
    gcd, x, _y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

def affine_decrypt(cipher, key):
    return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) 
					% 26) + ord('A')) for c in cipher ])

text = 'FEKHFMBABFKKH'
key = [17, 20]

affine_decrypted_text = affine_decrypt(text, key)

print('Decrypted Text: {}'.format(affine_decrypted_text))