""" There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with 
the kth person, and removing every successive kth person going clockwise until there is no one left. """

import sys

def survive(a, k):
    n = len(a)
    while (n >= k):
        a.extend(a[:k-1])
        del a[:k]
        n = len(a)
            
    return a

if __name__ == '__main__':
    print(survive(sys.argv[1].split(','), int(sys.argv[2])))