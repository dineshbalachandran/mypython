""" Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed. """


from string import ascii_lowercase

def decode(m):
    cd = dict()
    for k in range(0, 26):
        cd[k+1] = ascii_lowercase[k]
    
    def search(m):
        l = list()
        if len(m) == 0:
            l.append('')
            return l

        for i in range(1, len(m)+1):
            p = int(m[:i])
            if p > 26:
                break
            
            prefix = cd[p]
            for suffix in search(m[i:]):
                l.append(prefix + suffix)
            
        return l
    
    return search(m)

if __name__ == '__main__':
    print(decode("111"))