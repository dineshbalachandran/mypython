def unique(txt):
    s = set()
    i = 0
    while i < len(txt):
        if txt[i] in s:            
            break
        s.add(txt[i])
        i += 1
    if i == len(txt):
        print("String unique")
    else:
        print("String not unique")

if __name__ == '__main__':
    txt = input("Enter string: ")
    unique(txt)