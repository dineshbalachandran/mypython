""" Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, 
return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal]. """

class Trie:
    def __init__(self, c):        
        self.t = dict()
        self.c = c
    
    def add(self, s):                    
        if len(s) == 0:
            return

        i = ord(s[0])-97
        if i not in self.t:
            self.t[i] = Trie(s[0])
        self.t[i].add(s[1:])
    
    def query(self, s):
        l = []

        if len(s) == 0:
            return self.get()

        i = ord(s[0])-97
        if i not in self.t:
            return l

        for x in self.t[i].query(s[1:]):
            l.append(self.c+x)
        
        return l

    def get(self):
        l = []

        for i in self.t:
            for j in self.t[i].get():
                l.append(self.c + j)
            
        if len(l) == 0:
            l.append(self.c)
            
        return l

if __name__ == '__main__':
    t = Trie('')
    for s in ["dog", "deer", "deal", "dorm", "ear"]:
        t.add(s)
    print(t.query("da"))    