""" In front of you is a row of N coins, with values v1, v2, ..., vn.
You are asked to play the following game. You and an opponent take turns choosing either the first or last coin 
from the row, removing it from the row, and receiving the value of the coin.
Write a program that returns the maximum amount of money you can win with certainty, if you move first, 
assuming your opponent plays optimally. """



def pickCoins(v):
    i = 0
    j = len(v) - 1
    p1 = []
    p2 = []
    p = p1
    while (i <= j):
        if (v[i+1] + v[j] >= v[i] + v[j-1]):
            p.append(v[j])
            j = j - 1
        else:
            p.append(v[i])
            i = i + 1
        p = p2 if p is p1 else p1
    
    return (p1, p2)

# index out of bounds if only two coins
if __name__ == '__main__':
    print(pickCoins([2, 1, 6, 9]))