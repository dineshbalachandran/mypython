def steps(n):
    ways = [0]*(n+1)
    ways[1] = 1
    ways[2] = 2
    ways[3] = 4

    for i in range(4, n+1):
        ways[i] = ways[i-1] + ways[i-2] + ways[i-3]

    return ways[n]

def test(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = test(n-1, memo) + test(n-2, memo) + test(n-3, memo)
        return memo[n]

if __name__ == "__main__":
    n = int(input("Enter no. of steps: "))
    print(steps(n))
    print(test(n, [-1]*(n+1)))