'''
Created on 29Jul.,2017

@author: DINESHKB
'''

if __name__ == '__main__':
    value = int(input('Enter a positive integer:'))
    
    pwr = 2    
    while pwr < 6:
        root = 0        
        while root**pwr < abs(value):
            root += 1
        if root**pwr == abs(value):
            print(root, '**', pwr, 'is equal to', value)
            break
        else:
            pwr += 1
    
    if pwr == 6:
        print('no pair exists')
            
        
    