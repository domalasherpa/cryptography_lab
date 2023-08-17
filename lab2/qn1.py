
# x at bit 23
#initial : mapped to 62 place
#final : 62 is mapped to 23 place -> gives x
def permutationBox(box, data):
    output=""
    for i in box:
        output += data[i - 1]
    return output

if __name__ == "__main__":
    initialBox =[58, 50, 42, 34, 26, 18, 10, 2, #8
                60, 52, 44, 36, 28, 20, 12, 4,  #16
                62, 54, 46, 38, 30, 22, 14, 6,  #24
                64, 56, 48, 40, 32, 24, 16, 8, #32
                57, 49, 41, 33, 25, 17, 9 ,1    #40
                ,59, 51, 43, 35, 27, 19, 11, 3, #48
                61, 53, 45, 37, 29, 21, 13, 5,  #56
                63, 55, 47, 39, 31, 23, 15, 7]  #64

    final = [40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9 ,49 ,17 ,57 ,25]

    data = "0000000000000000000000000000000000000000000000000000000000000001"
    iBoxOutput = permutationBox(initialBox, data)
    fBoxOutput = permutationBox(final, data)

    print(f"The output of the initial permutation box for {data} is \n{iBoxOutput}.\n")
    print(f"The output of the final permutation box for {data} is \n{fBoxOutput}")
    





