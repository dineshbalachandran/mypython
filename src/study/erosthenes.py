'''
Created on 18Jul.,2017

@author: DINESHKB
'''

def generate_primes(limit):
    
    prime = [True]*limit
    p = 2
    
    while True:
        while p < limit and not prime[p]:            
            p += 1
        
        if p >= limit:
            break
                
        k = p + p
        
        while k < limit:
            prime[k] = False
            k = k + p
        
        yield p        
        p += 1


if __name__ == '__main__':
    
    for pr in generate_primes(100): print(pr)
        
    