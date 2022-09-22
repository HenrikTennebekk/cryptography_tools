#The information we already know
q = 331
g = 3
public_a = 10
public_b = 8

#These start at 0, but increase as we test them
private_a = 0
private_b = 0

#Checks if private key could be used to create public key until it succedes
while g ** private_a % q != public_a:
    private_a += 1
while g ** private_b % q != public_b:
    private_b += 1

print(f"Private Key a: {private_a}")
print(f"Private Key b: {private_b}")
#Uses the now available private key to find out what the shared secret key is
print(f"Shared secret key: {public_a ** private_b % q}")
print(f"Shared secret key: {public_b ** private_a % q}")