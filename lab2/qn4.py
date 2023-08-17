#program to demonstrate key generation process in des

#key with parity bits
# parity bits [8,16,24,32,40,48,56,64]  // multiple of 8
# 1. drop parity bit output -> 56 bits
# circular shift left the 56 bit
# 2. Divide into two halves left -> 28 bits  -> left box 28 bits
#  right -> 28 bits -> right box 28bits
# 3. key selection matrix

def shift(key, round):
    shiftByOne = [1, 2, 9, 16] #other shift by two
    if(round in shiftByOne):
        key = key[1:] + key[0:1]
    else:
        key = key[2:] + key[0:2]
    return key

    
def main(key):
    leftSelection = [57, 49, 41, 33, 25, 17, 9,
                      1, 58, 50, 42, 34, 26, 18,
                     10, 2, 59, 51, 43, 35, 27,
                     19, 11, 3, 60, 52, 44, 36]

    rightSelection = [63,55, 47, 39, 31, 23, 15,
                       7,62, 54, 46, 38, 30, 22,
                      14,6, 61, 53, 45, 37, 29,
                      21,13, 5, 28, 20, 12, 4]
                    
    keySelection = [14, 17, 11, 24, 1, 5, 3, 28,
                    15, 6, 21, 10, 23, 19, 12, 4,
                    26, 8, 16, 7, 27, 20, 13, 2,
                    41, 52, 31, 37, 47, 55, 30, 40,
                    51, 45, 33, 48, 44, 49, 39, 56,
                    34, 53, 46, 42, 50, 36, 29, 32]
    
    keys = ["" for i in range(16)]
    
    for i in range(16):
        key = shift(key, i + 1)
        left = ""
        right = ""
        for j in range(28): #removing parity bit and divide into two halves
            left += key[leftSelection[j] - 1] 
            right += key[rightSelection[j] - 1]
        
        for j in keySelection: #key ith selection / compression
            keys[i] += key[j]
        
    for i in range(16):
        print(f"key {i + 1}  : {keys[i]}")


if __name__ == "__main__":
    # key = input("Enter inital 64 bit key: ")
    key = "1001100100111011100110010011101110011001001110110011101110011001"
    main(key)
