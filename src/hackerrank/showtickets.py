
from functools import reduce

def timetaken(tickets, position):
    time = 0
    for i in range(len(tickets)):
        if i <= position:
            time += min(tickets[position], tickets[i])
        else:
            time += min(tickets[position] - 1, tickets[i]) 
    
    return time

if __name__ == "__main__":    
    tickets = [int(x) for x in (input("Enter tickets in order comma separated: ").split(','))]
    position = int(input("Enter Jesse's position in queue: "))
    #print(timetaken(tickets, position))

    print(reduce((lambda acc, ticket: (acc[0] + 1, acc[1] + (min(tickets[position], ticket) if acc[0] <= position else min(tickets[position] - 1, ticket)))), [], (0, 0) ))