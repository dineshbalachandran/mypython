"""You are given an array of integers representing the prices of a single stock on various days 
(each index in the array represents a different day). You are also given an integer k, which represents 
the number of transactions you are allowed to make. One transaction consists of buying the stock on a 
given day and selling it on another, later day. Write a function that returns the maximum profit that 
you can make buying and selling the stock, given k transactions. Note that you can only hold 1 share of
the stock at a time; in other words you cannot buy more than 1 share of stock on any given day, and you 
cannot buy a share of the stock if you are still holding another share.

Sample input: [5,11,3,50,60,90],2
Sample output: 93(Buy:5, Sell:11, Buy:3, Sell:90)"""


def solution(prices, k):
    if not len(prices):
        return 0

    profits = [[0 for d in prices] for t in range(k+1)]

    for t in range(1, k+1):
        maxthusfar = float("-inf")
        for d in range(1, len(prices)):
            maxthusfar = max(maxthusfar, profits[t-1][d-1] - prices[d-1])
            profits[t][d] = max(profits[t][d-1], maxthusfar + prices[d])
    return profits[-1][-1]

def maxprofit(prices, k):            
    s =""
    mbuy = prices[0]
    msell = mbuy
    for i in range(1, len(prices)):
        if prices[i] > msell:
            msell = prices[i]
        if prices[i] < mbuy:
            if (msell-mbuy) > 0:                
                s += " Buy:" + str(mbuy) + " Sell:" + str(msell)
            mbuy = prices[i]
            msell = 0

    if (msell-mbuy) > 0:                
        s += " Buy:" + str(mbuy) + " Sell:" + str(msell)
    
    return s

if __name__ == '__main__':
    print(solution([5,4,100,50,60,90],2))

