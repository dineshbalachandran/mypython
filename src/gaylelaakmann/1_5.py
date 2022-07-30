from pdb import lasti2lineno


def oneedit(txt1, txt2):
    l1 = len(txt1)
    l2 = len(txt2)
    if l1 > l2 + 1 or l2 > l1 + 1:
        return False
    if l1 >= l2:
        shorttext = txt2
        longtext = txt1
    else:
        shorttext = txt1
        longtext = txt2

    i = 0
    j = 0
    edit = 0
    while i < len(shorttext):       
        if shorttext[i] != longtext[j]:
            edit += 1
            if len(shorttext) != len(longtext):
                j += 1
        if edit > 1:
            return False
        i += 1
        j += 1    
    return True

if __name__ == '__main__':
    txt1 = input("Enter first string: ")
    txt2 = input("Enter second string: ")    
    print("Is it one-edit away? {}".format(oneedit(txt1, txt2))) 