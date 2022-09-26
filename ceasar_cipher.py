def encrypt(m, k):
    chartset = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    c = ""

    for i in range(len(m)):
        c += chartset[(chartset.index(m[i]) + k) % len(chartset)]
    return c

def decrypt(c, k):
    chartset = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    m = ""

    for i in range(len(c)):
        m += chartset[(chartset.index(c[i]) - k) % len(chartset)]
    return m