'''
Created on 2Aug.,2017

@author: DINESHKB
'''

def create_max(num, k):
    """Create maximum number with k digits."""
    # your code here
    def find_max(num, k):
        k -= 1
        
        if k != 0:
            max_v = max(num[:-k])
            index = num[:-k].index(max_v)
        else:
            max_v = max(num)
            index = num.index(max_v)
            
        return (max_v, index)
     
    value = ''
    
    while k > 0:
        (max_v, index) = find_max(num, k)
        value += max_v
        
        num = num[index + 1:]        
        k -= 1
            
    return value

if __name__ == '__main__':
    print(create_max('912583', 2))
    