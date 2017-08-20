'''
Created on 2Aug.,2017

@author: DINESHKB
'''

def max_profit(prices):
    """Find maximum profit possible."""
    # your code here
    
    profit = 0
    
    if len(prices) == 0:
        return 0
    
    sell = prices[len(prices)-1]
    buy = sell
    
    for i in range(len(prices)-2, -1, -1):
        if prices[i] > sell or prices[i] > buy:            
            profit += sell - buy                
            sell = prices[i]
            buy = sell
        elif prices[i] < buy:
            buy = prices[i]

    profit += sell - buy
    return profit

if __name__ == '__main__':
    print(max_profit([1,6,5,2,8,1,4,5]))