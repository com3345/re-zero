'''
Page 36
Algorithm 2.18
Insert elem into dulLinklist before the elem with index i

        [8, 7] None
Index    0  1  2


>>> dul = Dulinkedlist([8, 7])
>>> dul
8<->7

>>> dul.insert_elem_with_index(-1, 99)
Traceback (most recent call last):
    ...
IndexError: Index invalid

>>> dul.insert_elem_with_index(3, 99)
Traceback (most recent call last):
    ...
IndexError: Index invalid

>>> dul.insert_elem_with_index(0, -99)
>>> dul
-99<->8<->7

>>> dul.insert_elem_with_index(3, 101)
>>> dul
-99<->8<->7<->101
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Dulinkedlist(object):
    def __init__(self, l):
        dummy = cur = Node(0)
        l = l[::-1]
        while l:
            node = Node(l.pop())
            cur.next = node
            node.prev = cur
            cur = cur.next
        self.head = dummy.next

    def __repr__(self):
        r = []
        node = self.head
        while node:
            r += [node.val]
            node = node.next
        return '<->'.join(map(str, r))

    def insert_elem_with_index(self, index, val):
        if index < 0:
            raise IndexError('Index invalid')
        dummy = cur = Node(0)
        cur.next = self.head
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if not cur:
            raise IndexError('Index invalid')
        new = Node(val)
        if not cur.next:
            cur.next = new
            new.prev = cur
        else:
            cur.next.prev, new.next = new, cur.next
            new.prev, cur.next = cur, new
        self.head = dummy.next


if __name__ == '__main__':
    import doctest
    doctest.testmod()
