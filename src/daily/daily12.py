""" There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters. """

def staircase(_n, _x):
    memo = dict()

    def _staircase(n, x):
        l = []
        if n == 0:
            l.append([])         
            return l
        
        if n in memo:
            return memo[n]
        
        for s in x:
            if n-s >= 0:
                for t in _staircase(n-s, x):
                    tmp = t.copy()
                    tmp.append(s)
                    l.append(tmp)
        
        memo[n] = l

        return memo[n]

    return _staircase(_n, _x)   

if __name__ == '__main__':
    r = staircase(5, [1, 2])
    print(len(r))
    for i in r:
        print(i)

