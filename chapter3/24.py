'''
Page 43
Algorithm 2.24(by myself)
Polynomial multiplication with linkedlist

a       = -98 +         32X^2 - 7X^3
b       = 33  - 12X^1 + 8X^2          + 12X^4

a * b   =   - 98    * (33  - 12X^1 + 8X^2 + 12X^4)
          + 32X^2   * (33  - 12X^1 + 8X^2 + 12X^4)
          + - 7X^3  * (33  - 12X^1 + 8X^2 + 12X^4)


>>> a = Mypoly([(98, 0), (32, 2), (-7, 4), (15, 6)])
>>> a
y = 98 + 32X^2 - 7X^4 + 15X^6

>>> b = Mypoly([(33, 0), (-12, 1), (8, 2), (12, 3)])
>>> b
y = 33 - 12X^1 + 8X^2 + 12X^3

>>> a.multiple_fast(b)
y = 5338 - 384X^2 + 340X^4 + 204X^6 - 56X^8 + 36X^12 + 180X^18

'''


from linkedlist import Polynomial, PNode


class Mypoly(Polynomial):
    def __init__(self, item):
        super().__init__(item)
        self.cur = self.head

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
                # new = PNode((p1.coef + p2.coef, p1.exp))
                # cur.next, new.next = new, p1.next
                cur.next = p1
                p1.coef += p2.coef
                p1, p2 = p1.next, p2.next
            cur = cur.next
        cur.next = p1 or p2
        self.head = dummy.next

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur is None:
            self.cur = self.head
            raise StopIteration()
        node = self.cur
        self.cur = self.cur.next
        return node

    def multiple_fast(self, multipled):
        d = {}
        for item in [(aa.coef * bb.coef, aa.exp * bb.exp) for bb in multipled for aa in self]:
            d[item[1]] = d.get(item[1], 0) + item[0]
        return Mypoly([(a, b) for b, a in d.items()])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
