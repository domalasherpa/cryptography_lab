
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    phi = 1
    factor = {}
    
#find the prime factors of the n
    for i in range(2, n + 1):
        if(n % i == 0):
            factor[i] = 1
            n /= i
            while(n % i == 0):
                factor[i] = factor.get(i)+ 1
                n /= i
        if(n <= 1):
            break
    print(factor)


    for key in factor.keys():
        phi *= pow(key, factor[key]) - pow(key, factor[key] - 1)
    
    print(phi)

    
