""" Given a stream of elements too large to store in memory, pick a random element from 
the stream with uniform probability. """

import random
count = 0
prev = 0

def pick(c):
    global count, prev    
    r = random.randint(0, count)
    count += 1
    if r == c:
        prev = r

    return prev

if __name__ == '__main__':
    for i in range(0, 10):
        print(pick(i))
