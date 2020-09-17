import math

def isPrime(x):
    if(x==2 or x==3): return True
    if(x%2==0 or x<2): return False

    for i in range(3,int((x/2)+1),2):
        if(x%i==0):
            return False      
        
    return True

# for x in range(0,10000):
#     print(str(x)+'  '+str(isPrime(x)))