class Graph_ES:
    def __init__(self, vs=set(), es=set()):
        self.V = vs
        self.E = es

    def __len__(self):
        return len(self.V)

    def __iter__(self):
        return iter(self.V)

    def add_vertex(self, v):
        self.V.add(v)

    def remove_vertex(self, v):
        if v in self.V:
            self.V.remove(v)
        else:
            raise KeyError

    def add_edge(self, e):
        self.E.add(e)

    def remove_edge(self, e):
        if e in self.E:
            self.E.remove(e)
        else:
            raise KeyError

    def _neighbors(self, v):
        nbrs = []
        for e in self.E:
            if e[0] == v:
                nbrs.append(e[1])
        return nbrs

class Graph_AS:
    def __init__(self, vs=set(), es={}):
        self.V = vs
        self.E = es

    def __len__(self):
        return len(self.V)

    def __iter__(self):
        return iter(self.V)

    def add_vertex(self, v):
        self.V.add(v)

    def remove_vertex(self, v):
        self.V.remove(v)

    def add_edge(self, e):
        if e[0] not in self.E:
            self.E[e[0]] = {e[1]}
        else:
            self.E[e[0]].add(e[1])

    def remove_edge(self, e):
        if e[0] in self.E:
            self.E[e[0]].remove(e[1])
            if len(self.E[e[0]]) == 0:
                self.E.pop(e[0])
        else:
            raise KeyError
    
    def _neighbors(self, v):
        return self.E[v]