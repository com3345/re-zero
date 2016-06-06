'''
Page 30
Algorithm 2.11
Struct linkedlist reversely(by myself)

like [1, 5, 2, 3]
            3
         2->3
      5->2->3
   1->5->2->3

>>> l = Linkedlist([1, 5, 2, 3])
>>> l
1->5->2->3
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Linkedlist(object):
    def __init__(self, l):
        cur = Node(l.pop())
        while l:
            last = cur
            cur = Node(l.pop())
            cur.next = last
        self.head = cur

    def __repr__(self):
        r = []
        node = self.head
        while node:
            r += [node.val]
            node = node.next
        return '->'.join(map(str, r))
