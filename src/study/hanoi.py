'''
Created on 24 Sep. 2018

@author: DINESHKB
'''

import sys

def hanoi(left):
    _move(left,[],[],'1','2','3',0)

def _move(left, mid, right, lname, mname, rname, count):
    
    #base case: when both stacks are empty, job done, stop
    if len(left) == 0 and len(mid) == 0:
        print ("Number of moves:", count)
        return
    
    try:
        l = left[-1]
    except IndexError:
        l = sys.maxsize
    
    try:
        m = mid[-1]
    except IndexError:
        m = sys.maxsize
        
    if (l < m):
        left.pop()
        mid.append(l)
        print(lname, "->", mname, ":", l)
    else:
        mid.pop()
        left.append(m)
        print(mname, "->", lname, ":", m)
       
    _move(right, left, mid, rname, lname, mname, count+1)

if __name__ == '__main__':
    
    stack = [6,5,4,3,2,1]    
    hanoi(stack)