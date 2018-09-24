'''
Created on 5 Dec. 2017

@author: DINESHKB
'''

def rom(numeral):    
    dic = { 'I' : 1, 'II' : 2, 'III' : 3, 'IV' : 4, 'V' : 5, 'VI' : 6, 'VII' : 7, 
           'VIII' : 8, 'IX' : 9, 'XIX' : 19, 'X' : 10, 'XX' : 20, 'XXX' : 30, 'XL' : 40, 'L' : 50}
    
    val = 0
    
    if numeral == 'XIX' or numeral == 'IX':
        val = dic[numeral]
        return val
    
    for f in ['XL', 'XXX', 'XX', 'X']:
        i = numeral.find(f)
        if i != -1:
            val = dic[f]          
            if i + len(f) == len(numeral):
                return val
            p = numeral[i+len(f):]
            val += dic[p]
            return val
    
    val = dic[numeral]    
   
    return val

def lex(name):    
    n = name.split(' ')    
    return (n[0] + str(rom(n[1])).zfill(2))

def getsortednames(names):    
    return sorted(names, key=lex)

if __name__ == '__main__':
    l = ['Phillip XL', 'Phillip L']
    print(sorted(l))
    print(getsortednames(l))