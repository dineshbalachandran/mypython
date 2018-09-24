'''
Created on 22 Apr. 2018

@author: DINESHKB
'''

def getBinaryRep(n, numdigits):
    result = ''
    while n > 0:
        result = str(n%2) + result
        n = n//2
    if len(result) > numdigits:
        raise ValueError('not enough digits')
    for _ in range(numdigits - len(result)):
        result = '0' + result
    
    return result

def genpowerset(L):
    powerset = []
    for i in range(0, 2**len(L)):
        binstr = getBinaryRep(i, len(L))
        subset = []
        for j in range(len(L)):
            if binstr[j] == '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset

if __name__ == '__main__':
    print(genpowerset([1,2,3]))
    
    