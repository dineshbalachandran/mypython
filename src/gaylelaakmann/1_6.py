def compress(txt):
    if len(txt) < 3:
        return txt

    out = []
    currchar = txt[0]
    count = 0
    for char in txt:
        if char != currchar:
            out.append(currchar)
            out.append(str(count))
            currchar = char
            count = 1
        else:
            count += 1
    
    out.append(currchar)
    out.append(str(count))
    compresstxt = ''.join(out)

    return compresstxt if len(compresstxt) < len(txt) else txt



if __name__ == '__main__':
    txt = input("String to compress: ")
    print("Compressed string: {}".format(compress(txt)))