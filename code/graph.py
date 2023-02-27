class EdgeSet:
    def __init__(self):
        self.V = set()
        self.E = set()

    def add_vertex(self, v):
        self.V.add(v)

    def remove_vertex(self, v):
        self.v.remove(v)

    def add_edge(self, e):
        self.E.add(e)

    def remove_edge(self, e):
        self.E.remove(e)

    def __iter__(self): 
        return iter(self.V) # a set is by default iterable

    def _neighbors(self, v):
        nbrs = set()
        for e in self.E:
            # edges that look like (v, ?)
            if e[0] == v: nbrs.add(e[1])
        return nbrs

class Graph(EdgeSet):
    pass

class AdjacencySet:
    def __init__(self):
        self.V = set()
        self.nbrs = dict()

    def add_vertex(self, v):
        self.V.add(v)

    def remove_vertex(self, v):
        self.V.remove(v)

    def add_edge(self, e):
        a, b = e # assumes e = (x, y)
        if a not in self.nbrs: 
            self.nbrs[a] = {b}
        else: 
            self.nbrs[a].add(b)

    def remove_edge(self, e):
        a, b = e
        self.nbrs[a].remove(b)

        if len(self.nbrs[a]) == 0:
            self.nbrs.pop(a)

    def __iter__(self):
        return iter(self.V)

    def _neighbors(self, v):
        return iter(self.nbrs[v])

class Graph(AdjacencySet): # dfs goes down the deepest path and then recurses back up the recursive stack
    def dfs(self, v):
        path = [v]
        return self._dfs(v, path)

    def _dfs(self, v, path):
        for n in self._neighbors(v):
            if n not in path:
                path.append(n)
                return self._dfs(n, path)
        return path

if __name__ == '__main__':
    # Store the following graph:
    # 1--4
    # |\ |
    # | \|
    # 2--3

    g = Graph()
    vs = {1, 2, 3, 4} # note that it is not necessarily ordered
    es = {(1,2), (1,3), (1,4), (2, 1), (2, 3), (3, 1), (3, 2), (3, 4), (4, 1), (4, 3)}

    for v in vs: g.add_vertex(v)
    for e in es: g.add_edge(e)

    for v in g: 
        print("v = {}, neighbors:".format(v))
        for nbr in g._neighbors(v):
            print("\t{}".format(nbr))
        print()