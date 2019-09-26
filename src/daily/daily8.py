""" A unival tree (which stands for "universal value") is a tree where all nodes under it have the 
same value. Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1 """

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def unival(n):
    c = 0
    queue = []
    queue.append(n)

    while len(queue) != 0:
        n = queue.pop(0)
        if n != None:
            left = n.val if n.left == None else n.left.val
            right = n.val if n.right == None else n.right.val
            if left == n.val and right == n.val:
                c += 1               
            queue.append(n.left)
            queue.append(n.right)

    return c

if __name__ == '__main__':
    node = Node(0, Node(1), Node(0, Node(1, Node(1, Node(1), Node(1)), Node(0))))
    print(unival(node))