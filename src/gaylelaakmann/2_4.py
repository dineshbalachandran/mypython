class LinkedList:
    def __init__(self, values):        
        self.head = None
        prev = None
        for value in values:
            n = LinkedList.Node(value, None)
            if self.head == None:
                self.head = n
            else:
                prev.next = n
            prev = n

    class Node:
        def __init__(self, value, next):
            self.value =  value
            self.next = next

    def __str__(self):
        curr = self.head
        nodes = []
        while curr != None:
            nodes.append(str(curr.value))
            curr = curr.next
        
        return '->'.join(nodes)


def partitionList(ll, partition):
    greater = None   
    
    curr = ll.head

    while curr != None:
        if curr.value >= partition: 
            if greater == None:
                greater = curr
        else:
            if greater != None:
                temp = greater.value
                greater.value = curr.value
                curr.value = temp
                
                greater = greater.next
        
        curr = curr.next

    return ll

if __name__ == "__main__":
    nodestring = input("Enter comma separated number values: ")
    partition = int(input("Enter partition: "))
    nodes = [int(x) for x in nodestring.split(',')]
    print(partitionList(LinkedList(nodes), partition))
