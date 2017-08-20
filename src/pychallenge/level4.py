'''
Created on 24Jul.,2017

@author: DINESHKB
'''

import urllib.request
import re

if __name__ == '__main__':
    link = r"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    n = "80119"
    
    for _ in range(400):
        with urllib.request.urlopen(link + n) as ll:
            s = ll.read().decode('utf-8')
            m = re.search(r"\d+$", s)            
            if m is not None: 
                n = m.group() 
            else:
                print(s)
                break    
    print(n)
        
            
        