'''
Page 42
Algorithm 2.22
Implementation of a linklist of polynomial

terms       = [(2,8), (-2,23), (77, 0), (0, 0)]
Polynomial  : y = 77 - 2X^8 - 2X^23

>>> p = Polynomial([(2,8), (-2,23), (77, 0), (0, 0)])
>>> p
y = 77 + 2X^8 - 2X^23
'''


class Node(object):
    def __init__(self, term):
        self.coef, self.exp = term
        self.next = None


class Polynomial(object):
    def __init__(self, l):
        l.sort(key=lambda x: x[1], reverse=True)
        # l = l[::-1]
        dummy = cur = Node((0, 0))
        while l:
            cur.next = Node(l.pop())
            cur = cur.next
        self.head = dummy.next

    def __repr__(self):
        r = []
        node = self.head
        while node:
            if node.exp != 0:
                if node.coef < 0:
                    r += ['- {0}X^{1}'.format(abs(node.coef), node.exp)]
                elif node.coef > 0:
                    r += ['+ {0}X^{1}'.format(node.coef, node.exp)]
            else:
                if node.coef < 0:
                    r += ['-' + str(abs(node.coef))]
                elif node.coef > 0:
                    r += [str(node.coef)]
            node = node.next
        return 'y = ' + ' '.join(r)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
