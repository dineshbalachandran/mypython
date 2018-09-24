'''
Created on 2Aug.,2017

@author: DINESHKB
'''

def string_permutations(s):
    """find string permutations."""
    # your code here
    
    l = []
    
    if len(s) == 0:
        return ['']
           
    for i in range(0,len(s)):
        for j in string_permutations(s[:i] + s[i+1:]):
            l.append(s[i] + j)
    
    return l

if __name__ == '__main__':
    print(string_permutations('abc'))