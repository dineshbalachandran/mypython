

def istaircase(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache

def staircase(_n, X):
    memo = dict()
    
    def _staircase(n, X):        
        if n == 0:
            return [[]]

        if n in memo:
            return memo[n]
        
        r = []
        for i in X:
            if n-i >= 0:
                for t in _staircase(n-i, X):                    
                    s = t.copy()
                    s.append(i)
                    r.append(s)        
        memo[n] = r 

        return memo[n]

    return _staircase(_n, X)



if __name__ == '__main__':
    m = istaircase(4, [1,2,3])
    print(m[4])
    
    l = staircase(4, [1,2,3])
    print(len(l))
    
    for i in l:        
        print(i, end=" ")