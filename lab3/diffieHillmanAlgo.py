def findKey(yReceived, xAssumed, n):
    return (yReceived ** xAssumed) % n

if __name__ == "__main__":
    # alpha=13 
    # n = 257
    alpha = int(input("Enter the alpha for both alice and bob: "))
    n = int(input("Enter the n for both alice and bob: "))
    
    xA, xB = 23, 57
    
    yA = (alpha ** xA) % n
    yB = (alpha ** xB) % n
    
    keyA = findKey(yB, xA, n)
    keyB = findKey(yA, xB, n)
    
    print("Key A: ", keyA, "\nKey B: ",keyB)
