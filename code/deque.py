class Deque: # pronounced "deck"
    def __init__(self):
        self._L = []

    # O(n)
    def add_first(self, item):
        self._L.insert(0, item)

    # O(1)
    def add_last(self, item):
        self._L.append(item)

    # O(n)
    def remove_first(self):
        return self._L.pop(0)

    # O(1)
    def remove_last(self):
        return self._L.pop()

if __name__ == '__main__':
    d = Deque()
    n = 10

    for i in range(n):
        d.add_first(i)

    for i in range(n):
        assert d.remove_last() == i

    print("add_first/remove_last work!")

    d = Deque()
    for i in range(n):
        d.add_last(i)

    for i in range(n):
        assert d.remove_first() == i

    print("add_last/remove_first work!")



