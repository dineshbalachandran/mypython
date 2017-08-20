'''
Created on 24Jul.,2017

@author: DINESHKB
'''

import pickle

if __name__ == '__main__':
        
    file = open(r"D:\workspace\mypython\data\pychallenge\level5.txt",'rb')    
    input_data = pickle.load(file)
    
    # the data provided is pickled in python 2, this gives an Unpickling Error in python 3
    
    print(input_data)
        