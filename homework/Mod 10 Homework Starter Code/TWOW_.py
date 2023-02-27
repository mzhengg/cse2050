class Person:
    def __init__(self, name, phase, cat=None):
        self.name = name
        self.phase = phase
        self.cat = cat

    def __eq__(self, other):
        return self.name == other.name

    def __le__(self, other):
        return self < other or self.equal(other)

    def __lt__(self, other):
        if self.cat is not None and other.cat is not None and self.phase == 1 and other.phase == 1:
            return not self.cat < other.cat
        elif self.cat is not None and other.cat is not None and self.phase == other.phase:
            return self.cat < other.cat
        else:
            return self.phase < other.phase

    def equal(self, other):
        if self.cat is not None and other.cat is not None:
            return self.phase == other.phase and self.cat == other.cat
        else:
            return self.phase == other.phase

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.phase, self.cat)

class Line:
    def __init__(self, n_avail, people=[]):
        self.n = n_avail
        self.L = []
        self.sold = []
        if len(people) > 0:
            for p in people:
                self.add_buyer(p)

    def __len__(self):
        return len(self.L)

    def add_buyer(self, person):
        if not isinstance(person, Person): raise TypeError
        if person in self.sold: raise KeyError
        self.L.append(person)
        self.upheap(len(self.L)-1)
        self.sold.append(person)

    def parent(self, i):
        return (i - 1) // 2

    def swap(self, a, b):
        L = self.L
        L[a], L[b] = L[b], L[a]

    def upheap(self, i):
        L = self.L
        parent = self.parent(i)
        if i > 0 and L[i] < L[parent]:
            self.swap(i, parent)
            self.upheap(parent)

    def sell_book(self):
        if self.n == 0: raise ValueError
        if len(self.L) == 0: raise IndexError
        
        output = self.L[0]
        self.L[0] = self.L[len(self.L)-1]
        self.L.pop()
        self.downheap(0)
        self.n -= 1
        return output

    def children(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        return range(left, min(len(self.L), right + 1))

    def downheap(self, i):
        L = self.L
        children = self.children(i)
        if children:
            child = min(children, key = lambda x: L[x])
            if L[child] < L[i]:
                self.swap(i, child)
                self.downheap(child)
    
    def add_copies(self, n):
        self.n += n

if __name__ == '__main__':
    p1 = Person('Jake', 3, 'GP')
    p2 = Person('Taylor Swift', 1, 'FR')
    p3 = Person('Noam Chomsky', 1, 'EL')
    people = {p1, p2, p3}
    line = Line(n_avail=2, people=people)
    assert len(line) == 3

    assert line.sell_book() == Person("Taylor Swift", 1, "FR")
    assert line.sell_book() == Person("Noam Chomsky", 1, "EL")
    try:
        line.sell_book()
    except:
        pass
    before = line.n
    line.add_copies(5)
    after = line.n
    assert (after-before) == 5
    assert line.sell_book() == Person("Jake", 3, "GP")

    try:
        line.add_buyer(p1)
    except:
        pass
    p4 = Person('Greninja', 2, 'K12')
    line.add_buyer(p4)
    assert line.sell_book() == Person("Greninja", 2, "K12")
