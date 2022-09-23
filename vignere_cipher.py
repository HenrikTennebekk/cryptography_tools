def encrypt(m, k):
    #The set of characters in the english alphabet
    chartset = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    #Makes a variable where the ciphertext will be stored
    c = ""
    #Loop that runs for the length of the message
    for i in range(len(m)):
        #Encrypts and adds the current letter to the variable c
        c += chartset[(chartset.index(m[i]) + chartset.index(k[i % len(k)])) % len(chartset)]
    #Returns ciphertext
    return c

def decrypt(c, k):
    #The set of characters in the english alphabet
    chartset = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    #Makes a variable where the message will be stored
    m = ""
    #Loop that runs for the length of the ciphertext
    for i in range(len(c)):
        #Decrypts and adds the current letter to the variable m
        m += chartset[(chartset.index(c[i]) - chartset.index(k[i % len(k)])) % len(chartset)]
    #Returns decrypted message
    return m