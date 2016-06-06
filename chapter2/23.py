'''
Page 43
Algorithm 2.23
Polynomial addition with linkedlist

a       = -98 +         32X^9 - 7X^32
b       = 33  - 12X^5 + 8X^9          + 12X^20000

a + b   = -65 - 12X^5 + 40X^9 - 7X^32 + 12X^20000

>>> a = Mypoly([(-98, 0), (32, 9), (-7, 32)])
>>> b = Mypoly([(33, 0), (-12, 5), (8, 9), (12, 20000)])
>>> a
y = -98 + 32X^9 - 7X^32
>>> b
y = 33 - 12X^5 + 8X^9 + 12X^20000
>>> a.add(b)
>>> a
y = -65 - 12X^5 + 40X^9 - 7X^32 + 12X^20000

'''


from linkedlist import Polynomial, PNode


class Mypoly(Polynomial):
    def add(self, added):
        dummy = cur = PNode((0, 0))
        p1, p2 = self.head, added.head
        while p1 and p2:
            if p1.exp < p2.exp:
                cur.next = p1
                p1 = p1.next
            elif p1.exp > p2.exp:
                cur.next = p2
                p2 = p2.next
            else:
                new = PNode((p1.coef + p2.coef, p1.exp))
                cur.next, new.next = new, p1.next
                p1, p2 = p1.next, p2.next
            cur = cur.next
        cur.next = p1 or p2
        self.head = dummy.next


if __name__ == '__main__':
    import doctest
    doctest.testmod()
