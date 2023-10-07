# SHA-512
This is the documentation of the implementation of the sha-512 algorithm in python programming language.

## Introduction
SHA-512 is a one way hashing algorithm to produce a unique message digest for an unique input.
SHA-512 produces a 512 bit message digest. The input message can of any length less  than $2^{64}$ bits. 

## Algorithm:
1.  Get the input from the user
2.  Convert the message into byte form
3.  Add length bit and padding bit if necessary
4. Divide the message into 1024 bit blocks if length of message + length > 1024 or if message > 896
5. Initialize the 80 words constant k
6. initialize the initial 8 words message digest.
7. Save the copy of message digest. mdCopy = md
8.  find the message digest for 80 rounds
9.  The output of the message digest will be the seed for the next message block.
10. Repeat from steps six until there are not 1024 bit blocks left.
11. Add the result of the last from the last block with the initial message digest. mdCopy + md. 

## Function used:

### getInput()

```python
    message = input("Enter the message: ") 
    message = message.encode('utf-8')
    message = hex(int.from_bytes(message, 'big'))[2:]
```
Input is taken from the user in plain text format. The input is then encoded to the 'utf-8' encoding using the encode function. The output of encode function is a "byte string" starting with b'. The byte string message is then converted to the int using the from_bytes method. And, then to the hexadecimal using hex. However, note that is not necessary to convert the int to hex. As later on the hexadecimal is converted to int for bitwise operations.

```python
    length = hex(len(message) * 4)
    padLen = 1024 - (len(message) * 4) % 1024
    padding = hex(int(pow(2, padLen - 1)))
    length = int(length, 16)
    padding = int(padding, 16)
    message = int(message, 16)
    message = hex(((message <<  padLen) | padding) << 128 | length)[2:]
```
The length of the hex message is calculatted using len() method. Since, each character in hexadecimal is of 4 bits. The length of the message is multiplied by 4. The length of the padding bit along with the length bit is calculatted. Note that, the size of length bit is not subtracted while calculatting the padding length. This is to ease the calculation of padding bit in the message. The padding bit starts with 1 with trailing zero. Thus, we can calculatte the padding by taking 2 to the power of length after message in 1024 bit block. The intial message is then left shifted by length of padding and 128 (padLen).
```
    message + 0 * (padding + length)
    or with padding gives 
    message + padding + 0 * 128
    or with length
    message + padding + length 
```

### w()
```python
    w = [0] * 80
    for j in range(80):
        if(j < 16):
            w[j] = int(message[j], 16)
        else:
            w[j] = (w[j - 16] ^ w[j - 14] ^ w[j - 8] ^ w[j - 3]) << 1 | (w[j - 16] ^ w[j - 14] ^ w[j - 8] ^ w[j - 3]) >> 63
```
w function return the 80 words (64 bits) for each rounds. The first initial 16 words are same as the 16 64 bit block from the message. The rest W16-W79 are calculatted using the xor of the previous words and then left circular shift by 1.


### rotate()

```python
    def rotate(E, first, second, third):
        bitSize = 64
        E1 = ((E >>  first) | (E << (bitSize - first))) & ((1 << bitSize) - 1) 
        E2 = ((E >>  second) | (E << (bitSize - second))) & ((1 << bitSize) - 1)
        E3 = ((E >>  third) | (E << (bitSize - third))) & ((1 << bitSize) - 1)
        return E1 ^ E2 ^ E3  #returns in integer
```

Rotate function gives the result of the circular right rotation of the blocks. The first, second and third is the specific length of bitwise shift for block A and E. The rotate function then return the xor operation of the shifted words.

### majority()
```python
    def majority(A, B, C):
        return (A & B) ^ (B & C) ^ (C & A)
```
The majority function is to calculate the bits for first word i.e A of the message digest.

### conditional()
```python
    def conditional(E, F, G):
        return (E & F) ^ ((~E) & G)
```
The conditional function is to calculate the bits for the fifth words i.e E of the message digest.

### mixer1()
```python
    def mixer2(E, F, G, H, W, K):
        return (conditional(E, F, G) + rotate(E, 14,18, 41) + W + K + H) % pow(2, 64) 
```
The mixer1 function return the sum of the result by conditional function, the rotate operation and the corresponding constant K and w for that round, and the H word of the message digest. The sum is then mod by $2^{64}$ to make sure the result lies under 64 bit representation.

### mixer2()
```python
    def mixer1(A, B, C):
        return (majority(A, B, C) + rotate(A, 28, 34, 39)) % pow(2, 64)  
```
The mixer2 return the sum of the result by the majority function and the rotate function. The result is then mod by $2^{64}$ to make sure results lies under 64 bit representation

### rounds()
```python
def round(md, w, k):
    d = md[3]
    for i in range(7, 0, -1): 
        if(i == 0 or i == 4):
            continue
        md[i] = md[i - 1]
        
    mixer2Out = mixer2(md[4], md[5], md[6], md[7], w, k)
    md[4] = (d + mixer2Out) % pow(2, 64)    
    md[0] = (mixer1(md[0], md[1], md[2]) + mixer2Out) % pow(2, 64)
    return md
```
The round function emulates the operation that happens in each 80 rounds for a message block in sha-512. In each round, the 8 64 bit words are changed. The words except "A" and "E" of position "0" and "4" are copied to the corresponding right block. The word E is calcultted by sum of word "D" and output of mixer2(). The word A is then calulatted by sum of mixer1() and mixer2() with mod $2^{64}$. 

### sha512()

```python
for message in messageBlock:
        message = [message[i:i+16] for i in range(0, len(message), 16)] #dividing the message into 16 64 bit words to cal words for each round
        w = W(message)

        mdCopy = md.copy()
        for i in range(80): #eighty rounds for each 1024 bit block
            mdCopy = round(mdCopy, w[i], k[i])
        
```
In SHA-512 function constant k, md are initialized. Then, the messageBlock return by getInput() is iterated by message. And, each message is of 1024 bit. The message is then divied into 16 bit words to calculatted the words (W) for the rounds. The initial hash/message digest is then copied to mdCopy. The mdCopy is calculated for each rounds and for each blocks using the round(). 

```python
print("The message digest for the given message is: \n")
    for i in range(8) :
        md[i] = hex((md[i] + mdCopy[i]) % pow(2, 64))
        print(md[i][2:])
    print("\n")
```

Then, the result of the last round is added with the initial hash/md seed to calculate the 512 bit message digest for the given input. 


