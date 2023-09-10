import math
import random

if __name__ == "__main__":
    n = int(input("Enter test number: "))
    rounds = int(input("Enter no of rounds: "))
    u = 1
    primeProbab = 0
    notPrimeProbab = 0
    k = 1
    
#a number is even then it is composite
    if(n % 2 == 0 and n != 2): 
        print(f"{n} is  a composite number.")
#could be composite
    else:
        #n-1 = u * s^k
        while((n-1) % (2 ** k) == 0):
            k+= 1
        k -= 1

#required no of rounds
    for _ in range(rounds):
        u = (n-1) / (2 ** k)
        a = random.randint(2, n-1)
        b = (a ** u) % n

        print(f"k: {k}, u: {u}, a: {a}, b:{b}")

        if(b == 1 or b == n-1):
            primeProbab += 1
        
        for i in range(k):
            b = (b**b) % n
            if(b == n-1):
                primeProbab += 1
            if(b == 1):
                notPrimeProbab += 1
    
    print(f"Prime Probability: {primeProbab}\nNot Prime Probability: {notPrimeProbab}")





