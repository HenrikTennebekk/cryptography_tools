import math

def encrypt(m, k):
    c = ""
    for i in range(len(k)):
        for j in range(math.ceil(len(m) / len(k))):
            if len(k) * j + (int(k[i]) - 1) < len(m):
                c += m[len(k) * j + (int(k[i]) - 1)]
    return c