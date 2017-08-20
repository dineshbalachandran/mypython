'''
Created on 20Jul.,2017

@author: DINESHKB
'''


def abc():
    a = deff()
    for i in a:
        yield i
    yield 'abc'

def deff():
    a = ijk()
    for i in a:
        yield i
    yield 'deff'

def ijk():
    for i in (1,2,3):
        yield i
    yield 'ijk'


l = [1,2,3]

def mno():
    for j in l:
        yield j

if __name__ == '__main__':
    # k = abc()
    
    k = mno()
    
    for i in k: 
        print (i)
        if i < 6:
            l.append(i+3)