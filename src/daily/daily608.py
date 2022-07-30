# Given a start word, an end word, and a dictionary of valid words, find the shortest transformation sequence 
# from start to end such that only one letter is changed at each step of the sequence, and each transformed word 
# exists in the dictionary. If there is no possible transformation, return null. Each word in the dictionary have 
# the same length as start and end and is lowercase.
# For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"}, 
# return ["dog", "dot", "dat", "cat"].
# Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, return null as there is no possible 
# transformation from dog to cat.


from queue import Queue

def trans_sequence(dictionary, start, end):    
    
    def search_list(word):        
        s = set()
        for i in range(len(end)):           
            item = word[0:i] + end[i] + word[i+1:]
            if item != word:
                s.add(item)        
        return s
    
    if end not in dictionary:
        return None
    
    q = Queue(len(dictionary))
    l = []
    l.append(start)
    q.put(l)

    result = None
    t_dict = set(dictionary)
    while not q.empty():
        sequence = q.get()        
        for item in search_list(sequence[-1]):
            if item in t_dict:
                l = list(sequence)
                l.append(item)
                q.put(l)
                t_dict.remove(item)
                if item == end:
                    result = l
                    break        
    
    return result
   
   
if __name__ == '__main__':
    print(trans_sequence({"dot", "dop", "dat", "cat"}, "dog", "cat"))
    print(trans_sequence({"dot", "dop", "cat"}, "dog", "cat"))
    print(trans_sequence({"dot", "dop", "dag", "cog", "cot", "cat"}, "dog", "cat"))
    print(trans_sequence({"dat", "dop", "dag", "dot", "cog", "cot", "cat"}, "dog", "cat"))