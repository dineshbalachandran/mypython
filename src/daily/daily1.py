""" Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17. """

def addup(l, k):
    store = set()
    for i in l:
        if i in store:
            return (k-i, i)
        store.add(k-i)

    return ()

if __name__ == '__main__':
    print(addup([10,15,3,7], 18))
