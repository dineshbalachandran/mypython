from collections import deque

def reachable(target):

    def bfs():

        q = deque()
        q.append((0,0,0))
        
        options = [(0,1,1), (1,0,1), (1,1,0)]
        
        while q:
            curr = q.popleft()
            print(curr)
            if curr == target:
                return True
            
            for option in options:
                nextvalue = tuple(map(sum, zip(curr, option)))
                print(nextvalue)
                if nextvalue[0] > target[0] or nextvalue[1] > target[1] or nextvalue[2] > target[2]:
                    continue                
                q.append(nextvalue)
        
        return False
    
    return bfs()

if __name__ == "__main__":
    T = int(input())
    M = int(input())
    
    count = 0
    for _ in range(T):
        target = tuple(int(x) for x in input().split(' '))
        count = count + 1 if reachable(target) else 0
    print(count)
