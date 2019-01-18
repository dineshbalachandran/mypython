'''
Created on 24 Sep. 2018

@author: DINESHKB
'''

import sys

def hanoi(stack):
    _move1(stack,'1','2','3')

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


def _move1(stack, lname, mname, rname):
    
    moves = 0
    disks = len(stack)
    left = stack
    mid = []
    right = []    
    
    while (len(right) != disks):    
        
        l = left[-1] if len(left) != 0 else disks+1 #a value higher than other disks to facilitate check below
        m = mid[-1] if len(mid) != 0 else disks+1        
            
        if (l < m):            
            mid.append(left.pop())
            print(lname, "->", mname, ": ", l, sep="")
        else:            
            left.append(mid.pop())
            print(mname, "->", lname, ": ", m, sep="")  
        
        moves = moves + 1
        
        (t, tname) = (left, lname)
        (left, lname) = (right, rname)
        (right, rname) = (mid, mname)
        (mid, mname) = (t, tname)       
        
    print("Number of moves:", moves)
    return

if __name__ == '__main__':
    
    stack = [4,3,2,1]    
    hanoi(stack)