class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Mapping:
    def __init__(self):
        self._len = 0
        self._n_buckets = 100
        self._L = [[] for i in range(self._n_buckets)]

    def rehash(self):
        self._n_buckets *= 2
        new_L = [[] for i in range(self._n_buckets)]
        for bucket in self._L:
            for entry in bucket:
                new_bucket = self.hash(entry.key)
                new_l[new_bucket].append(entry)
        self._L = new_L[:]
        
    def hash(self, key): # If we use the lazy update for the number of buckets we can get O(1) average running time
        return key % self._n_buckets
    
    def __setitem__(self, key, value):
        bucket = self.hash(key)
        # Case 1: key in dict
        for entry in self._L[bucket]:
            if entry.key == key:
                entry.value = value
                return

        # Case 2: key not in dict
        self._L[bucket].append(Entry(key, value))
        self._len += 1

        if len(self) > self._n_buckets: self.rehash()

    def __len__(self):
        return self._len

    def __getitem__(self, key):
        bucket = self.hash(key)
        for entry in self._L[bucket]:
            if entry.key == key:
                return entry.value
        raise KeyError("key {} not in Mapping".format(key))

if __name__ == '__main__':
    m = Mapping()
    n = 100
    for i in range(n):
        m[i] = str(i)

    for i in range(n):
        assert m[i] == str(i)
