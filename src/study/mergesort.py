'''
Created on 4Aug.,2017

@author: DINESHKB
'''


def mergesort(nums):
    """Mergesort."""
    # your code here
    
    def merge(a, b):
        """Merge two lists sorted in descending order."""
        # your code here
    
        m = []
        i, j = 0, 0
        
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                m.append(a[i])
                i += 1
            else:
                m.append(b[j])
                j += 1
        
        m += a[i:] + b[j:]
        
        return m
    
    def _mergesort(nums, lo, hi):
        
        res = []
        
        if lo < hi:
            mid = lo + (hi - lo)//2
            a = _mergesort(nums, lo, mid)
            b = _mergesort(nums, mid+1, hi)
            
            res = merge(a, b)
        else:
            res.append(nums[lo])
               
        return res
    
    return _mergesort(nums, 0, len(nums)-1)

if __name__ == '__main__':
    print(mergesort([2, 9, 2, 3, 5, 8, 1]))