import numpy as np
import math

def mod(x):
    if(x < 0):
        return 26 - (-x) % 26
    else:
        return x % 26

def createTextMat(cols, col1, text, mode):
    k = 0
    flag = 0
    A = [[ 23 for i in range(col1)] for j in range(cols)] # x = 23
    inr = 1

    if(mode == 1):
        inr = cols
  
    for i in range(cols):
        if mode == 1:
            k = i
        for j in range(0, col1):
            A[i][j] = ord(text[k]) - 97 #normalizing to 0
            if(k == len(text)):
                flag = 1
                break
            k += inr
        if(flag):
            break
    return A


def hill(rows, cols, col1, key, text, mode):
    
    A = createTextMat(cols, col1, text, mode)
    if(mode == -1):#find the inverse of the key
        det = mod(round(np.linalg.det(key))) 
        invDet = 0
        for i in range(26):
            if mod(det * i) == 1:
                invDet = i  #inverse of det
                break
        if(not invDet):
            print("Inverse modulo doesnot exist..")
            return
        adj = np.linalg.inv(key) * np.linalg.det(key)   #Ainv = adj * 1/det -> adj = Ain * det
        key = invDet * adj  #key inverse for the decryption

    key = [[mod(round(key[i][j])) for i in range(rows)] for j in range(cols)]   #mod 26 
    C = np.matmul(key, A)
    C = [[chr(mod(C[i][j]) + 97) for i in range(cols)] for j in range(col1)]
    C = np.transpose(C)

    if(mode == -1):
        C = np.transpose(C)
        temp = cols
        cols = col1
        col1 = temp
    
    cipher = ""

    for i in range(cols):
        for j in range(col1):
            cipher += C[i][j]
    return cipher


if __name__ == "__main__":

    rows = int(input("Enter the number of rows of key: "))
    cols = int(input("Enter the number of cols of key: "))
    key = [[0 for i in range(rows)] for j in range(cols)]

    print("Enter the key matrix: ")
    for i in range(rows):
        for j in range(cols):
            key[i][j] = int(input())
    
    text = input("Enter the text: ").lower()
    mode = int(input("Enter 1 for encryption and -1 for decrytion: "))

    #making sure cols can be divided equally
    col1 = len(text) // cols
    if(len(text) / cols > len(text) //cols):
        col1 += 1

    print(hill(rows, cols, col1, key, text, mode))
