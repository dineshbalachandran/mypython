'''
Created on 2Aug.,2017

@author: DINESHKB
'''

def simplify_path(path):
    """Simplify Unix-style file path."""
    # your code here
    
    stack = []    
    s = ''
    stack.append('')   
    
    # constraint: 'path' always begins with a '/'
    for i in range(1, len(path) + 1):
        if i == len(path) or path[i] == '/':
            if s == '..':
                if len(stack) > 1:
                    stack.pop()
            elif s == '.':
                pass
            elif s != '':              
                stack.append(s)            
            s = ''
        else:
            s += path[i]            
    
    if len(stack) == 1:
        stack.append('')
            
    return '/'.join(stack)

if __name__ == '__main__':
    print(simplify_path('/foo///..//bar/.'))