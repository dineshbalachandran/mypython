""" Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA". """

import sys

def mapping(n):
    s = ""
    a = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
    while (n > 0):
        d = n % 26
        n = int(n / 26) if d != 0 else int((n-1) / 26)
        s = s + a[d]

    return s[::-1]

if __name__ == '__main__':
    print(mapping(int(sys.argv[1])))
