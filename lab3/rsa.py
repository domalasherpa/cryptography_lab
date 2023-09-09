
import random

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def alice():
    p, q = input("Enter two prime numbers: ").split()
    p = int(p)
    q = int(q)

    n = p * q
    phi = (p - 1) * (q - 1)

    #public key
    while True:
        publicKey = random.randint(1, phi) 
        if(gcd(phi, publicKey) == 1):
            break

    #private key
    for i in range(1, phi):
        if (i * publicKey) % phi == 1:
            privatekey = i
            break

    message = bob(n, publicKey)
    print(f"Encrypted message by Bob: {message}")
    message = (message ** privatekey) % n
    print(f"Decrypted message by Alice: {message}")

def bob(n, publicKey):
    msg = int(input(f"Enter a message to send BoB less than {n}: "))
    return (msg ** publicKey) % n 

if __name__ == "__main__":
    alice() 
