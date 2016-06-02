'''
Page 31
Algorithm 2.2 merge list

Merge two sorted lists into one. There can be duplicates.

>>> a, b = [1, 2, 3], [0, 2, 4]
>>> c = merge_two_list(a, b)
>>> c
[0, 1, 2, 2, 3, 4]
>>> a, b = [1, 2, 2, 3], [3, 3, 4]
>>> c = merge_two_list(a, b)
>>> c
[1, 2, 2, 3, 3, 3, 4]

'''


def merge_two_list(a, b):

    c = []
    p1, p2 = 0, 0
    n1, n2 = len(a), len(b)
    while p1 < n1 and p2 < n2:
        if a[p1] < b[p2]:
            c += [a[p1]]
            p1 += 1
        else:
            c += [b[p2]]
            p2 += 1
    if p1 < n1:
        c += a[p1:]
    if p2 < n2:
        c += b[p2:]
    return c

if __name__ == '__main__':
    import doctest
    doctest.testmod()
