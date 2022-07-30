""" Let's define a "sevenish" number to be one which is either a power of 7, or the sum of unique powers of 7. 
The first few sevenish numbers are 1, 7, 8, 49, and so on. Create an algorithm to find the nth sevenish number. """

import math, sys

def sevenish(n):

    if n == 0:
        return 0
    
    x = math.floor(math.log(n,2))

    return math.pow(7, x) + sevenish(n-math.pow(2, x))

if __name__ == '__main__':
    print(int(sevenish(int(sys.argv[1]))))