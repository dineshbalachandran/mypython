'''
Created on 26 Nov. 2017

@author: DINESHKB
'''

import collections

def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

def combo(code, nword):
    
    result = []
    
    if (nword == 1):
        result.append(code)
        return result
    
    i = 1
    while (True):
        f = code[0:i]
        s = code[i:]
        
        if (len(s) >= (nword - 1) and len(f) <= 4):            
            for c in combo(s, nword-1):
                result.append([f, c])
        else:
            break
        
        i += 1
        
    return result

def morse(word):
    lkp = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.',
            'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..',
            'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-',
            'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--',
            'x':'-..-', 'y':'-.--', 'z':'--..'}
    
    code = ''
    for l in word:
        code += lkp[l]
    
    l = []
    for c in combo(code, len(word)):
        t = tuple(flatten(c))        
        l.append(t)
        
    vl = []
    for e in l:
        i = 0
        while (i < len(e)):            
            if e[i] not in lkp.values():   
                break
            i += 1
            
        if (i == len(e)):          
            vl.append(e)    
       
    return set(vl)

if __name__ == '__main__':
    print(len(morse("infy")))