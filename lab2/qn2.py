
def main(R):
    pbox = [32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1]

    exR = ""
    for i in pbox:
        exR += R[i - 1]
    
    return exR

if __name__ == "__main__":

    # R = input("Enter the 32 bit : ")
    R = "00010001000100010001000100010001"
    exR = main(R)
    print("Expanded key is ", exR)

    





