def railfence(text, key, mode):
    k = 0
    flag = 0

    cols = len(text) // key

    if(len(text) / key > len(text) // key):
        cols = cols+ 1
    
    rfmat = [['x' for i in range(cols)] for j in range(key)]
    if(mode == -1): #mode -1 for decryption and 1 for encryption
        temp = cols
        cols = key
        key = temp

    for i in range(0, cols):
        for j in range(0, key):
            if(mode == -1): #adding just rows by rows: encryption
                rfmat[i][j] = text[k] 
            else:#adding cols by cols for decryption
                rfmat[j][i] = text[k]
            k += 1
            if(k == len(text)):
                flag = 1
                break
        
        if(flag):
            break

    cipher = ""
    for i in range(0, key):
        for j in range(0, cols):
            if(mode == -1):
                cipher += rfmat[j][i]   #reading from the rows first in decrytion
            else:
                cipher += rfmat[i][j] #reading from the cols first in encryption

    return cipher
        

if __name__ == "__main__":
    text = input("Enter a text: ")
    key = int(input("Enter a key: "))
    mode = int(input("Enter 1 for encrypt and -1 for decrypt: "))
    text = text.replace(" ", "")
    print(f"Cipher: {railfence(text, key, mode)}")
