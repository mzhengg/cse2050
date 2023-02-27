class Entry:
    def __init__(self, pos, high, low):
        self.pos = pos
        self.high = high
        self.low = low

class TempMap:
    def __init__(self):
        self.buckets = 1
        self.L = [[] for i in range(self.buckets)]
        self.len = 0

    def __contains__(self, pos):
        rounded_pos = (round(pos[0], 1), round(pos[1], 1))
        bucket = self.hash(rounded_pos)

        for e in self.L[bucket]:
            if rounded_pos == (round(e.pos[0], 1), round(e.pos[1], 1)):
                return True
        
        return False

    def __getitem__(self, pos):
        rounded_pos = (round(pos[0], 1), round(pos[1], 1))
        bucket = self.hash(rounded_pos)

        for e in self.L[bucket]:
            if rounded_pos == (round(e.pos[0], 1), round(e.pos[1], 1)):
                return (e.low, e.high)

        raise KeyError

    def hash(self, item):
        return hash(item) % self.buckets

    def rehash_1(self):
        self.buckets *= 2
        new_L = [[] for i in range(self.buckets)]

        for bucket in self.L:
            for entry in bucket:
                rounded_pos = (round(entry.pos[0], 1), round(entry.pos[1], 1))
                new_bucket = self.hash(rounded_pos)
                new_L[new_bucket].append(entry)
        
        self.L = new_L

    def rehash_2(self):
        if self.len == 0:
            return

        self.buckets = self.buckets // 2
        new_L = [[] for i in range(self.buckets)]

        for bucket in self.L:
            for entry in bucket:
                rounded_pos = (round(entry.pos[0], 1), round(entry.pos[1], 1))
                new_bucket = self.hash(rounded_pos)
                new_L[new_bucket].append(entry)
        
        self.L = new_L

    def add_report(self, pos, temp):
        rounded_pos = (round(pos[0], 1), round(pos[1], 1))
        bucket = self.hash(rounded_pos)

        for e in self.L[bucket]:
            if rounded_pos == (round(e.pos[0], 1), round(e.pos[1], 1)):
                e.low = min(e.low, e.high, temp)
                e.high = max(e.low, e.high, temp)
                return

        self.L[bucket].append(Entry(pos, temp, temp))
        self.len += 1

        if self.len > self.buckets:
            self.rehash_1()

    def remove_pos(self, pos):
        rounded_pos = (round(pos[0], 1), round(pos[1], 1))
        bucket = self.hash(rounded_pos)

        for e in self.L[bucket]:
            if rounded_pos == (round(e.pos[0], 1), round(e.pos[1], 1)):
                self.L[bucket].remove(e)
                self.len -= 1
                if self.len < (self.buckets + 2) // 2:
                    self.rehash_2()
                return

        raise KeyError