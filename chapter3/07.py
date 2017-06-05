'''
Page 26
Algorithm 2.7
Merge two linked lists

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

    def __repr__(self):
        r = []
        node = self.head
        while node:
            r += [node.val]
            node = node.next
        return '->'.join(map(str, r))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
