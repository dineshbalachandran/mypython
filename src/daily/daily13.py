""" Given an integer k and a string s, find the length of the longest substring that contains at most 
k distinct characters. For example, given s = "abcba" and k = 2, the longest substring with k 
distinct characters is "bcb". """

def distinct(s, k):
    b = 0
    mb, me = 0, 0
    t = dict()

    for i in range(1, len(s)+1):
        c = s[i-1:i]
        t[c] = i-1
        if len(t) > k:
            if i-b > me-mb:
                me = i - 1
                mb = b
        
            #reset window start 'b'
            x = min(t, key=t.get)
            b = t[x] + 1
            del t[x]
        
    if len(s)-b > me-mb:
        me = len(s)
        mb = b

    return s[mb:me]

if __name__ == '__main__':
    print(distinct("aabacbebeb", 2))