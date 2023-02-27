class Queue():
    def __init__(self):
        self.L = []

    def enqueue(self, item):
        self.L.append(item)

    def dequeue(self):
        if len(self.L) > 0: return self.L.pop(0)
        else: return None

class ContactGraph:
    def __init__(self, V=set(), E=set()):
        self.V = V
        self.E = set()
        for a, b in E: self.add_edge(a, b)

    def add_edge(self, a, b):
        self.E.add((a, b))

    def __iter__(self):
        return iter(self.V)

    def neighbors(self, v):
        nbrs = []
        for e in self.E:
            a, b = e
            if v == a:
                nbrs.append(b)
        return iter(nbrs)

    def all_contacts(self, v):
        tree = {v: None}
        self._all_contacts(v, tree)
        return iter(tree)

    def _all_contacts(self, v, tree):
        for n in self.neighbors(v):
            if n not in tree:
                tree[n] = v
                self._all_contacts(n, tree)

    def group_contacts(self, V):
        g_cntcs = set()
        for v in V:
            for e in self.E:
                a, b = e
                if (v == a) and (b not in V):
                    g_cntcs.add(b)
        return iter(g_cntcs)

    def contacts(self, v, d):
        tree = {}
        cntcs = []
        tovisit = Queue()
        tovisit.enqueue((None, v, 0))
        while tovisit:
            try:
                a, b, c = tovisit.dequeue()
            except:
                break
            if b not in tree and c <= d:
                tree[b] = a
                cntcs.append((b, c))
                for n in self.neighbors(b):
                    tovisit.enqueue((b, n, c+1))
        return iter(cntcs)

class MutualContactGraph(ContactGraph):
    def __init__(self, V=set(), E=set()):
        super().__init__(V, E)

    def add_edge(self, a, b):
        self.E.add((a, b))
        self.E.add((b, a))

if __name__ == '__main__':
    V = [1, 2, 3, 4, 5, 6]
    E = [(1, 2), (2, 3), (3, 5), (5, 6), (5, 4), (4, 2), (5, 2)]
    G1 = ContactGraph(V, E)
    G2 = MutualContactGraph(V, E)

    #print("iterator")
    #for v in G1: print(v, end='')
    #print()
    #for v in G2: print(v, end='')
    #print()

    #print("neighbors")
    #for n in G1.neighbors(2): print(n, end=' ')
    #print()
    #for n in G2.neighbors(2): print(n, end=' ')
    #print()

    #print("all_contacts")
    #for c in G1.all_contacts(1): print(c, end=' ')
    #print()
    #for c in G2.all_contacts(1): print(c, end=' ')
    #print()

    #print("group_contacts")
    #for c in G1.group_contacts([1, 3]): print(c, end=' ')
    #print()
    #for c in G2.group_contacts([2, 3]): print(c, end=' ')
    #print()

    print("contacts")
    for c in G1.contacts(3, 2): print(c, end=' ')
    print()
    for c in G2.contacts(4, 2): print(c, end=' ')
    print()