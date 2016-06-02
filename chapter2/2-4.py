'''
Page 34
Algorithm 2.4 insert elem into list

Insert element into list at index without built-in insert() function
if index >= len(l) then insert the elem at the end of the list
if index < 0 then insert the elem at the start of the list

>>> l = Mylist([1,2,3])
>>> l.insert_elem(9, 1)
>>> l
[1, 9, 2, 3]
>>> l.insert_elem(8, -2)
>>> l
[8, 1, 9, 2, 3]
>>> l.insert_elem(3, 4)
>>> l
[8, 1, 9, 2, 3, 3]

'''


class Mylist(list):

    def insert_elem(self, elem, index):
        if index < 0:
            index = 0
        if index > len(self) - 1:
            index = len(self) - 1
        self[index + 1:] = self[index:]
        self[index] = elem

if __name__ == '__main__':
    import doctest
    doctest.testmod()
