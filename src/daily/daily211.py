""" Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. 
For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7]. """

import sys

def matchpat(s, p):    
    i = 0
    r = []
    slen = len(s)
    plen = len(p)
    while (i <= slen-plen):
        j = 0
        while (j < plen):
            if s[i:i+1] == p[j:j+1]:
                j = j + 1
            else:
                break
            i = i + 1
        if (j == plen):
            r.append(i-plen)
        i = i + 1

    return r

if __name__ == '__main__':
    print(matchpat(sys.argv[1], sys.argv[2]))
