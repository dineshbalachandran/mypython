'''
Created on 20Jul.,2017

@author: DINESHKB
'''

class Node(object):
    def __init__(self, value, left, right):
        self._value = value
        self._left = left
        self._right = right
        
    @property
    def value(self):
        return self._value
    
    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left
        
    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right
        
    def __iter__(self):
        return inorder(self)

# a recursive generator
def inorder(node):
    if node:
        for x in inorder(node.left):
            #print('left')            
            yield x
        yield node
        for x in inorder(node.right):
            #print('right')            
            yield x

def generateTree():
    
    root = Node(0, None, None)
    n = root
    
    for i in range(1, 5):
        l = Node(i, None, None)
        r = Node(i+10, None, None)
        
        n.left = l
        n.right = r
        
        n = l
    
    return root

if __name__ == '__main__':
    
    root= generateTree();
    
    it = iter(root)
    
    for j in it:
        print (j.value)
        
    