'''
Page 34
Algorithm 2.5 remove elem in list

Totally same as 2.4 if 'insert' replaced with 'remove'

>>> l = Mylist([1, 2, 3, 4, 5])
>>> l.remove_elem(0)
>>> l
[2, 3, 4, 5]
>>> l.remove_elem(3)
>>> l
[2, 3, 4]
>>> l.remove_elem(1)
>>> l
[2, 4]


'''


class Mylist(list):

    def remove_elem(self, index):
        if index < 0:
            index = 0
        if index > len(self) - 1:
            index = len(self) - 1
        self[index:] = self[index + 1:]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
