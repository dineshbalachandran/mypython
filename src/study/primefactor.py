'''
Created on 18Jul.,2017

@author: DINESHKB
'''


import math

from study import test

def primefactor(n):
    
    primes = []
    if test.is_prime(n):
        return n
    else:
        r = [2] + list(range(3, int(math.sqrt(n) + 1), 2))        
        for k in r:
            if n % k == 0: 
                primes.append(primefactor(k))
                primes.append(primefactor(int(n/k)))
    
    return primes    

def gen_prime_factors(n):

    r = [2] + list(range(3, int(math.sqrt(n) + 1), 2))        
    for k in r:
        if n % k == 0 and test.is_prime(k):            
            yield k            
                
if __name__ == '__main__':
        
    no = 60
    
    print (primefactor(no))
    for factor in gen_prime_factors(no): print(factor)