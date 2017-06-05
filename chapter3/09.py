'''
Page 29
Algorithm 2.9
Insert elem into sorted linkedlist(by myself)

>>> l = Linkedlist([1, 2, 3, 3])
>>> l
1->2->3->3

>>> l.head.val
1

>>> r = Linkedlist([0, 2, 5])
>>> r
0->2->5

>>> l.merge(r)
>>> l
0->1->2->2->3->3->5

New test cases for new method:

>>> l.insert_elem(-1)
>>> l
-1->0->1->2->2->3->3->5

>>> l.insert_elem(1)
>>> l
-1->0->1->1->2->2->3->3->5

>>> l.insert_elem(99)
>>> l
-1->0->1->1->2->2->3->3->5->99
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Linkedlist(object):
    def __init__(self, l):
        dummy = cur = Node(0)
        l = l[::-1]
        while l:
            cur.next = Node(l.pop())
            cur = cur.next
        self.head = dummy.next

    def __repr__(self):
        r = []
        node = self.head
        while node:
            r += [node.val]
            node = node.next
        return '->'.join(map(str, r))

    def merge(self, l):
        dummy = cur = Node(0)
        c1, c2 = self.head, l.head
        while c1 and c2:
            if c1.val < c2.val:
                cur.next = c1
                c1 = c1.next
            else:
                cur.next = c2
                c2 = c2.next
            cur = cur.next
        cur.next = c1 or c2
        self.head = dummy.next

    # new method insert
    def insert_elem(self, val):
        dummy = cur = Node(0)
        cur.next = self.head
        while cur.next and cur.next.val < val:
            cur = cur.next
        new = Node(val)
        new.next, cur.next = cur.next, new
        self.head = dummy.next
    # end

if __name__ == '__main__':
    import doctest
    doctest.testmod()
