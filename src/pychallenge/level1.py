'''
Created on 17Jul.,2017

@author: DINESHKB
'''

if __name__ == '__main__':
    from_str = 'abcdefghijklmnopqrstuvwxyz'
    to_str = 'cdefghijklmnopqrstuvwxyzab'
    transform = str.maketrans(from_str,to_str)
    result = 'map'.translate(transform)
    print(result)