'''
Created on 25Jul.,2017

@author: DINESHKB
'''

import zipfile
import re

if __name__ == '__main__':
    
    n = '90052'
    s = ''
    with zipfile.ZipFile(r"D:\workspace\mypython\data\pychallenge\level6.zip") as myzip:
        while True:
            with myzip.open(n + '.txt') as myfile:                                                
                m = re.search(r"\d+$", myfile.read().decode('utf-8'))            
                if m is not None: 
                    n = m.group()                    
                    s += myzip.getinfo(n + '.txt').comment.decode('utf-8')                    
                else:
                    print(s)
                    break
        
        