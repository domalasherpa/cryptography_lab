import random

def encryption(e1, e2, p,PlainText):
    e = random.randint(1, p-1)  #private key
    C1 = (e1 ** e) % p
    C2 = (PlainText * (e2 ** e)) % p
    return C1, C2

def keyGeneration(): 
    p =  997  #prime number
    e1 =  7  #primitive root
    d = random.randint(1, p-1)  #private key
    e2 = (e1 ** d) % p
    return e1, e2, d,  p

def decryption(d, p, C1, C2):
    for i in range(p):
        if((pow(C1, d) * i) % p == 1):
            C1inv = i
    P = C2 * C1inv % p
    return P

if __name__ == "__main__":
    e1, e2, d , p = keyGeneration()
    PlainText = int(input(f"Enter a plain text under {p}: "))

    C1, C2= encryption(e1, e2, p, PlainText)
    print(f"Cipher: {C1}, {C2}")
    P = decryption(d, p, C1, C2)
    print(f"Plain text: {P}")
