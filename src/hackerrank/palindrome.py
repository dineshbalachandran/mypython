'''
Created on 26 Nov. 2017

@author: DINESHKB
'''

def nextpal(num):
    
    l = len(num)
    m = (l + 1) //2
    left = num[:m]
    np_left = str(int(left) + 1)
    np_right = np_left[:l-m]
    np_right = np_right[::-1]
    
    return (np_left + np_right)
    
if __name__ == '__main__':
    print(nextpal("12344321"))