def palindrome(txt):
    counts = {}
    for char in txt:        
        if char == ' ':
            continue
        count = counts.setdefault(char, 0)
        counts[char] += 1
    odd = 0
    print(counts)
    for char in counts:
        if counts[char] % 2 != 0:
            odd += 1
        if odd > 1:
            return False
    return True

if __name__ == '__main__':
    txt = input("Enter string: ")    
    print("Permutation is a palindrome? {}".format(palindrome(txt.lower())))