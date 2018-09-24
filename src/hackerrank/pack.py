'''
Created on 5 Dec. 2017

@author: DINESHKB
'''
def pack(s):
    
    c = [int(i) for i in s.split(' ')]
    st = []
    
    l = len(c)
    
    while (l > 0):
        m = max(c)
        
        mat = [t for t in enumerate(c) if t[1] == m]               
        
        i = mat[-1][0] #the last index
        print(i)
        
        st.append(m) #add the match to stack
        
        j= range(i, l)
        
        c = [t[1] for t in enumerate(c) if (t[0] not in j)]        
        
        l = len(c)
        
    print(st)
    
    return    

if __name__ == '__main__':
    pack("16 4 8 2 8 16")