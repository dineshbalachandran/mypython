'''
Created on 26 Nov. 2017

@author: DINESHKB
'''

def nextpal(num):
    l = len(num)
    odd = l % 2 == 1
    if odd:
        m = l//2
        left = num[:m]
        right = num[m+1:]
        rev_left = left[::-1]
        np_left = str(int(left + num[m]) + 1) if int(right) >= int(rev_left) else left + num[m]
        np_right = np_left[:l-m-1][::-1]
    else:
        m = l//2
        left = num[:m]
        right = num[m:]
        rev_left = left[::-1]
        np_left = str(int(left)+1) if int(right) >= int(rev_left) else str(left)
        np_right = np_left[::-1]
    
    return (np_left + np_right)
    
if __name__ == '__main__':
    print(nextpal("99"))