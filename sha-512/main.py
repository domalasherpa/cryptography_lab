#sha 512
'''
To do 

    # -Find k - default takens 
    -message chunks
    -padding
    -length
    # -message digest - default taken

'''

def majority(A, B, C):
    # (a AND b) xor (b and c) xor (c and a)
    return (A & B) ^ (B & C) ^ (C & A)


def conditional(E, F, G):
    #(e and f) xor (not e and g)
    return (E & F) ^ ((~E) & G)


'''
for a : first= 28, second= 34, third= 39
for b: first=14, second=18, third=41
'''
def rotate(E, first, second, third):
    E1, E2, E2 = E
    E1 = (E >> first) | (E << (64 - first)) & 0xffffffff
    E2 = (E >> second) | (E << (64 - second)) & 0xffffffff
    E3 = (E >> third) | (E << (64 - third)) & 0xffffffff
    return E1 ^ E2 ^ E3  #returns in integer


'''
    E = mixer2 + D
'''
def mixer2(E, F, G, H, W, K):
    return (conditional(E, F, G) + rotateE(E) + W + K + H) % pow(2, 64)   #mod 2 power 64 


'''
    A = mixer1 + mixer2
'''
def mixer1(A, B, C):
    return (majority(A, B, C) + rotateA(A)) % pow(2, 64)  #mod 2^64


'''
    takes the 512 bit message digest
    message digest is a dict of 8 64bit words
    A, B , C, D, E, F, G, H
    0, 1,  2, 3, 4, 5, 6, 7
'''
def round(md, w, k):

    #shifting the words : B->C, C->D, E->F, F->G, G->H, except for A and E
    d = md[3]
    for i in range(7, 0, -1):
        if(i == 0 or i == 4):
            continue

        md[i] = md[i - 1]

    mixer2Out = mixer2(md[4], md[5], md[6], md[7], w, k)
    md[4] = (d + mixer2Out) % pow(2, 64)     # e = d + mixer2 mod 2^64
    md[0] = (mixer1(A, B, C) + mixer2Out) % pow(2, 64)# a= mixer1 + mixer2 mod 2^64

    return md




def main():
#get the message
#find the padding bits
#append the padding bits
#append the length of the message
#break the message into 1024 bit blocks
#calculate the number of chunks

    message = input("Enter the message: ")  
    message = message.encode('utf-8')   #encode the message to utf-8
    message = bin(int.from_bytes(message, 'big'))[2:]  #convert the message to binary

    if(len(message) / 1024 > 0): #message is greater than 896 bits
         #break the message into 1024 bit blocks
        length = bin(len(message)).zfill(128)
        padding = (len(message) + 128) % 1024
        if(padding != 0):
            padding = 1 + zfill(padding - 1)
        message = message + padding + length
        #left to divide the message into 1024 bit chunks
    else:
        padding = 896 - len(message)
        if(padding != 0):
            padding = 1 + zfill(padding - 1
        length = bin(len(message)).zfill(128)
        message = message + padding + length


    K = [
        0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc,
        0x3956c25bf348b538, 0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118,
        0xd807aa98a3030242, 0x12835b0145706fbe, 0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2,
        0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 0xc19bf174cf692694,
        0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
        0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5,
        0x983e5152ee66dfab, 0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4,
        0xc6e00bf33da88fc2, 0xd5a79147930aa725, 0x06ca6351e003826f, 0x142929670a0e6e70,
        0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 0x53380d139d95b3df,
        0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b,
        0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30,
        0xd192e819d6ef5218, 0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8,
        0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8,
        0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 0x682e6ff3d6b2b8a3,
        0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec,
        0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b,
        0xca273eceea26619c, 0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178,
        0x06f067aa72176fba, 0x0a637dc5a2c898a6, 0x113f9804bef90dae, 0x1b710b35131c471b,
        0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 0x431d67c49c100d4c,
        0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817
    ]

    md = [
        0x6a09e667f3bcc908,
        0xbb67ae8584caa73b,
        0x3c6ef372fe94f82b,
        0xa54ff53a5f1d36f1,
        0x510e527fade682d1,
        0x9b05688c2b3e6c1f,
        0x1f83d9abfb41bd6b,
        0x5be0cd19137e2179
    ]


    for i in messageBlocks:
        for j in range(80):

            '''
                finding the words for each rounds
            '''
            if(j < 16):
                w[i] = message[i]
            else:
                w[i] = (w[j - 16] ^ w[j - 14] ^ w[j - 8] ^ w[j - 3]) << 1 | (w[j - 16] ^ w[j - 14] ^ w[j - 8] ^ w[j - 3]) >> 63

            
            md = round(md, w, k)
    
if __name__ == "__main__":
    K()