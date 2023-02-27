class CustomSet:
    def __init__(self):
        self.buckets = 100
        self.set = [[] for i in range(self.buckets)]
        self.len = 0
    
    def __len__(self):
        return self.len

    def _hash(self, item):
        return hash(item) % self.buckets

    def __contains__(self, item):
        bucket = self._hash(item)

        for val in self.set[bucket]:
            if item == val:
                return True
        return False

    def rehash(self):
        self.buckets *= 2
        new_set = [[] for i in range(self.buckets)]

        for bucket in self.set:
            for item in bucket:
                b_val = self._hash(item)
                new_set[b_val].append(item)

    def add(self, item):
        bucket = self._hash(item)
        
        for val in self.set[bucket]:
            if item == val:
                return

        self.set[bucket].append(item)
        self.len += 1

        if self.len > self.buckets:
            self.rehash

    def remove(self, item):
        bucket = self._hash(item)

        if item in self.set[bucket]:
            self.set[bucket].remove(item)
            self.len -= 1
        else:
            raise ValueError

if __name__ == '__main__':
    my_set = CustomSet()
    assert len(my_set) == 0
    for i in range(10):
        my_set.add(i)
        assert i in my_set
    assert len(my_set) == 10

    assert not 10 in my_set

    for i in range(10):
        my_set.remove(i)
        assert not i in my_set

    try:
        my_set.remove(1000)
    except ValueError:
        pass

    cs = CustomSet()
    assert len(cs) == 0
    for i in range(100):
        cs.add(i)
        assert len(cs) == i+1
        
    for i in range(100):
        cs.remove(i)
        assert len(cs) == 99-i
