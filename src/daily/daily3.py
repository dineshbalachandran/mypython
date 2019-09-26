""" Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
and deserialize(s), which deserializes the string back into the tree.
For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left' """

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deserialize(s):
    lst = [None]
    i = 0

    si = 0
    while si < len(s):        
        ei = s.index(';', si)
        val = s[si:ei]
        
        n = Node(val) if val != '' else None
        
        i += 1
        lst.insert(i, n)

        p = lst[int(i/2)]        
        if p != None:
            if i%2 == 0:
                p.left = n
            else:
                p.right = n
        
        si = ei + 1

    return lst[1]    

def serialize(n):    
    s = ""
    queue = []
    queue.append(n)

    while len(queue) != 0:
        n = queue.pop(0)
        if n != None:
            s += n.val        
            queue.append(n.left)
            queue.append(n.right)
        s += ';'

    return s

if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(deserialize(serialize(node)).left.left.val)