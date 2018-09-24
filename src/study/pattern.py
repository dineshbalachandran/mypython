'''
Created on 28Jul.,2017

@author: DINESHKB
'''

import random
import operator

oper = {'+': operator.add, 
        '-': operator.sub, 
        '*': operator.mul, 
        '/': operator.truediv }

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            opers = input_data_file.readline().split(',')            
            limit = int(opers[2])
            
        print (opers)              
        
        for _ in range(4):
            a = random.randint(1, limit)
            b = random.randint(1, limit)
            c = random.randint(1, limit)
            
            d = oper[opers[1]](oper[opers[0]](a, b), c)
            
            print((a,b,c,d))
        
        
    