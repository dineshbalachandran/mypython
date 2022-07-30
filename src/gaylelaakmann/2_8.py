class LinkedList:
    def __init__(self, values, loopIndex):        
        self.head = None
        prev = None
        loopstart = None        
        
        for i in range(len(values)):
            n = LinkedList.Node(values[i], None)
            if self.head == None:
                self.head = n
            else:
                prev.next = n
            prev = n

            if i == loopIndex:
                loopstart = n
            if loopIndex > 0 and i == len(values) - 1:
                n.next = loopstart              

    class Node:
        def __init__(self, value, next):
            self.value = value
            self.next = next

        def __str__(self):
            return self.value

    def __str__(self):
        curr = self.head
        nodes = []
        while curr != None:
            nodes.append(curr.value)
            curr = curr.next        
        return '->'.join(nodes)

def isLoopedList(ll):

    curr = ll.head
    runner = ll.head    

    while runner != None and runner.next != None:
        curr = curr.next
        runner =  runner.next.next 
        if runner == curr:
            break

    if runner == None or runner.next == None:
        return (None, False)
    
    #collides due to a loop in the list   
    curr = ll.head    
    while curr != runner: #find the start of the loop in the list
        curr = curr.next
        runner = runner.next         
    
    return (curr, True)

if __name__ == "__main__":    
    nodestring = input("Enter comma separated node values: ")    
    nodes = [x for x in nodestring.split(',')]
    loopIndex = int(input("Enter entry point of loop: "))    
    (loopStart, isLoop)= isLoopedList(LinkedList(nodes, loopIndex))
    value = loopStart.value if loopStart else None
    print("{}, {}".format(value, isLoop))