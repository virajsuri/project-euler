import numpy as np
import math
import datetime
start_time = datetime.datetime.now()

def sieve(n): 
    primes = []
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p+=1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers 
    for p in range(n + 1): 
        if prime[p]: 
            # print(p)
            primes.append(p)
    
    return primes

def circular():
    count = 0
    primes = np.array(sieve(1000000))

    for n in primes:
        if(('0' or '2' or '4' or '5' or '6' or '8') in str(n)):  
            continue

        length = int(math.log10(n)) + 1 #finds length of int without converting to str
        p = math.pow(10, length) - 1 #10^L(n) -1
        non_prime_found = False

        for y in range(1,length):
            #rotate
            n = (n + n%10 * p) / 10

            #check if rotation is prime
            if(n not in primes):
                non_prime_found = True
                break
        
        if(non_prime_found == False):
            count+=1
        
    print(count)

circular()
print((datetime.datetime.now()-start_time))