'''
Basic implementation of Linkedlist
'''


class LinkNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Linkedlist(object):
    def __init__(self, l):
        dummy = cur = LinkNode(0)
        l = l[::-1]
        while l:
            cur.next = LinkNode(l.pop())
            cur = cur.next
        self.head = dummy.next

    def __repr__(self):
        r = []
        node = self.head
        while node:
            r += [node.val]
            node = node.next
        return '->'.join(map(str, r))


class PNode(object):
    def __init__(self, term):
        self.coef, self.exp = term
        self.next = None


class Polynomial(object):
    def __init__(self, l):
        l.sort(key=lambda x: x[1])
        l = l[::-1]
        dummy = cur = PNode((0, 0))
        while l:
            cur.next = PNode(l.pop())
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
