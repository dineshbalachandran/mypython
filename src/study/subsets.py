'''
Created on 3Aug.,2017

@author: DINESHKB
'''

def subsets(s):
    """Find all possible subsets of a list."""
    # your code here
    
    def combo(st, k):
        
        l = []        
        
        i = 0
        while i < k:
            f = st[i:i+1]
            s = st[i+1:]
            l.append(f)
            if len(s) > 0: 
                for j in combo(s, len(s)):
                    l.append(f + ',' + j)           
            
            i += 1
            
        return l
    
    lst = combo(s, len(s))
    
    
    lst = [i.split(',') for i in lst]
    lst.append([])
    
    return lst

if __name__ == '__main__':
    print(subsets('abc'))