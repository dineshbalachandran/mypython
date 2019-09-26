""" Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3. """

import sys

def missing_On(a):
    s = set()
    v = sys.maxsize

    for e in a:
        s.add(e)

    for e in a:
        lv = e - 1
        hv = e + 1
        if hv > 0 and hv < v and hv not in s:
            v = hv
        if lv > 0 and lv < v and lv not in s :
            v = lv

    return v

def missing_O1(a):
    def segregate(a):
        j = 0
        for i in range(0, len(a)):
            if a[i] <= 0:
                t = a[i]
                a[i] = a[j]
                a[j] = t
                j += 1        
        return j
    
    def missing(a):
        size = len(a)
        for i in range(0, size):                    
            if a[i] <= size and a[i] > 0 and a[a[i]-1] > 0:
                a[a[i]-1] = -a[a[i]-1]
          
        for i in range(0, size):
            if a[i] > 0:
                return i+1
        
        return len(a)+1

    return missing(a[segregate(a):])

if __name__ == '__main__':
    print(missing_O1([0, -1, 2, 3, 99,100]))