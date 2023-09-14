

# def orderOfGroup(n):
#     #phi(n)
#     #no of coprimes in a group
    
# def orderOfElement(orderOfGroup, el):
#     #2^i ~= 1 (mod n)
#     # order = i

if __name__ == "__main__":
    n = int(input("Enter a number: "))

    primeRoots = []

    for i in range(2, n):
        power = 0
        flag = 0
        ranges = [i for i in range(1, n)]

        while(True):
        #if all the numbers have appeared
            if(not ranges):
                flag= 1
                break
        
        #if the numbers are repeating 
            if((i ** power) % n not in ranges):
                flag = 0
                break
            else:
                ranges.remove((i ** power) % n)
            
            power+=1

        if(flag):
            primeRoots.append(i)
    
    print(f"Prime roots of {n} are: {primeRoots} ")
            
        
            
