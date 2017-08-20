'''
Created on 25Jul.,2017

@author: DINESHKB
'''

from PIL import Image
import re

if __name__ == '__main__':
    im = Image.open(r"D:\workspace\mypython\data\pychallenge\level7.png")
    
    print(im.format, im.size, im.mode)
    
    l = []
        
    col, row = im.size
    
    print(im.size)
    
    gr = [im.getpixel((cl, row/2)) for cl in range(col)]
    print(gr)
    gr = gr[::7]
    print(gr)
    
    ords = [r for r, g, b, a in gr if r == g == b]
    
    print("".join(map(chr, ords)))
    nums = re.findall(r"\d+", "".join(map(chr, ords)))
    print("".join(map(chr, map(int, nums))))
    
            