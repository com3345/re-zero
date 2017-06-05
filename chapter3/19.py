'''
Page 36
Algorithm 2.19
delete elem from dulLinklist with index i

        [8, 7, 3] None
Index    0  1  2  3


>>> dul = Dulinkedlist([8, 7, 3])
>>> dul
8<->7<->3

>>> dul.delete_elem_with_index(-1)
Traceback (most recent call last):
    ...
IndexError: Index invalid

>>> dul.delete_elem_with_index(3)
Traceback (most recent call last):
    ...
IndexError: Index invalid

>>> dul.delete_elem_with_index(0)
>>> dul
7<->3

>>> dul.delete_elem_with_index(1)
>>> dul
7
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

    def delete_elem_with_index(self, index):
        if index < 0:
            raise IndexError('Index invalid')
        dummy = cur = Node(0)
        cur.next = self.head
        while cur.next and index > 0:
            cur = cur.next
            index -= 1
        if not cur.next:
            raise IndexError('Index invalid')
        if not cur.next.next:
            cur.next = None
        else:
            cur.next.next.prev = cur
            cur.next = cur.next.next
        self.head = dummy.next


if __name__ == '__main__':
    import doctest
    doctest.testmod()
