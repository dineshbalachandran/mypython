""" You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N. """

N = 3
count = 0
log = [''] * N

def record(order_id):
    global log, count, N    
    count += 1
    pos = count % N
    log[pos-1] = order_id

def get_last(i):
    pos = count%N + i
    if pos > N:
        pos = pos - N
    
    return log[pos-1]

if __name__ == '__main__':
    for i in ["a", "b", "c", "d", "e"]:
        record(i)
    
    print(get_last(2))