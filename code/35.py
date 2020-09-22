from isprime import isPrime
import datetime
start_time = datetime.datetime.now()
count = 0

for x in range(1,1000000,2):
    
    
    # print(x)
    x_string = str(x)
    if('0' in x_string[1:]
        or '4' in x_string[1:]
        or '6' in x_string[1:]
        or '8' in x_string[1:]
        ):
        # print(x_string)
        continue

    if(isPrime(x)):

        split = (str(x))
        non_prime_found = False
        
        for x in range(len(split)):
            split = split[1:] + split[:1]

            #if the rotation is not prime
            if(isPrime(int(split)) == False):
                non_prime_found = True
                break

        if(non_prime_found == False):
            count+=1

        non_prime=False

print(count+1)


end_time = datetime.datetime.now()
print((end_time-start_time))