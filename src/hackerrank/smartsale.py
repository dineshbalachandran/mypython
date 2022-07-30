from collections import defaultdict
def solve(n, ids, itemsremoved):
    bag = defaultdict(lambda:0)    
    for i in range(n):        
        bag[ids[i]] += 1    
    uniqueitems = len(bag)
    for count in sorted(bag.values()):
        if itemsremoved - count >= 0:
            uniqueitems -= 1
            itemsremoved -= count
            if itemsremoved <= 0:
                break
    return uniqueitems 

if __name__ == "__main__":    
    ids = [2,3,3,5,5,5,6,6,6,6,6]
    n = len(ids)
    itemsremoved = 5
    print(solve(n, ids, itemsremoved))