""" Given an array of integers, return a new array such that each element at index i of the new array 
is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division? """


def product(a):
    if len(a) == 0 or len(a) == 1:
        return []

    l = [1] * len(a)
    r = [1] * len(a)

    for i in range(1, len(a)):
        l[i] = l[i-1] * a[i-1]

    for i in range(len(a)-2, -1, -1):
        r[i] = r[i+1] * a[i+1]

    return [l[i] * r[i] for i in range(0, len(a))]


if __name__ == '__main__':
    print(product([3, 2, -1]))