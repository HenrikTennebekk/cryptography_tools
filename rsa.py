def find_key(p, q, e):
    #Makes an enitial variable for the key
    d = 0
    ø = (p - 1) * (q - 1)

    #Tests all possibilities for d untill it is the correct one
    for i in range(ø):
        if i * e % ø == 1:
            d = i
    return d

def encrypt(m, p, q, e):
    #Returns the encrypted message
    return m ** e % (p * q)

def decrypt(c, p, q, e):
    #Returns the decrypted message
    return c ** find_key(p, q, e) % (p * q)
