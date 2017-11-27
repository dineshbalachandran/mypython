'''
Created on 27 Nov. 2017

@author: DINESHKB
'''

def fishmoves(text):    
    data = text.split('#')
    fish = int(data[0])
    tank = [int(i) for i in data[1].split(",")]
    tank.sort()
    
    n = len(tank)
    a = 0
    t = []
    t.append([0, n])
    
    while (n > 0):
        if fish > tank[0]:
            fish += tank[0]
            tank.pop(0)
            n -= 1
        else:
            t.append([a, len(tank)])
            a += 1
            fish += (fish - 1)

    t.append([a, 0])
        
    return t

if __name__ == '__main__':
    print(fishmoves("10#9,20,25,100"))