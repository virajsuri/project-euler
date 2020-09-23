import numpy as np
import datetime
start_time = datetime.datetime.now()

count = 0
length = 1000000

def SieveOfEratosthenes(n): 
    primes = []
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers 
    for p in range(n + 1): 
        if prime[p]: 
            # print(p)
            primes.append(p)
    
    return primes


primes = np.array(SieveOfEratosthenes(length))
print('Primes generated')

for x in range(1, length, 2):
    if(('0' or '2' or '4' or '5' or '6' or '8') in str(x)):  
        continue
    
    if(x in primes):
        split = (str(x))
        non_prime_found = False
        
        #iterate through rotations
        for x in range(len(split)):
            split = split[1:] + split[:1]

            #if the rotation is not prime
            if(int(split) not in primes):
                non_prime_found = True
                break

        if(non_prime_found == False):
            count+=1

print(count+1) #add one to account for 2 being prime

end_time = datetime.datetime.now()
print((end_time-start_time))