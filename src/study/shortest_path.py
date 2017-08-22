'''
Created on 22 Aug. 2017

@author: DINESHKB
'''
# non optimized code
#
from operator import itemgetter

def shortest_path(g, u, v):
    """Find shortest path between u and v in g."""
    # your code here   
        
    def all_paths(g, u, v, path_so_far):
        paths = []
        
        for n in g[u]:
            if n not in path_so_far:
                if n == v:
                    path_so_far = path_so_far + n
                    paths.append(path_so_far)
                    return paths
                else:
                    paths = paths + all_paths(g, n, v, path_so_far+n)
        
        return paths
    
    paths = all_paths(g, u, v, u)
    
    return paths[min(enumerate([len(i) for i in paths]), key=itemgetter(1))[0]]

if __name__ == '__main__':
    graph = {'a': ['b'], 'b': ['a', 'c', 'd'], 'c': ['b', 'd', 'e'], 'd': ['b', 'c', 'f'], 
     'e': ['c', 'f', 'g'], 'f': ['d', 'e', 'g'], 'g': ['e', 'f']}
    start = 'a'
    end = 'g'
    #print(shortest_path({'a': [], 'b': []}, 'a', 'b'))
    print(shortest_path(graph, start, end))