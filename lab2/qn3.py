#working mechanism of sbox1 in des

def main(k):
    sbox = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 10, 3, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ]

    row = k[0] + k[5]
    col = k[1:5]

    print(f"Row: {row} \t Col: {col}")

    row = int(row, 2) #convert base 2 string to int
    col = int(col, 2)
    reduced = sbox[row][col]

    reduced = format(reduced, 'b') #returns binary string of corresponding int
    while(len(reduced) != 4): #creating output of a 4 bit
        reduced = "0" + reduced
  
    return reduced
    
    

if __name__ == "__main__":
    k = input("Enter 6 bit pbox output: ")
    sbox1 = main(k)

    print(f"Output of sbox 1 for {k} is {sbox1}")





