class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

class PQ_UL:
    def __init__(self):
        self.L = []
        self.len = 0

    def __len__(self):
        return self.len

    def insert(self, item, priority):
        self.L.append(Entry(item, priority))
        self.len += 1

    def find_min(self):
        if len(self.L) == 0:
            return None

        min_val = self.L[0]
        for item in self.L[1:]:
            if item.priority < min_val.priority:
                min_val = item

        return min_val

    def remove_min(self):
        if len(self.L) == 0:
            return None

        min_val = self.L[0]
        for item in self.L[1:]:
            if item.priority < min_val.priority:
                min_val = item
        
        self.L.remove(min_val)
        self.len -= 1
        return min_val

class PQ_OL:
    def __init__(self):
        self.L = []
        self.len = 0

    def __len__(self):
        return self.len

    def insert(self, item, priority):
        new_entry = Entry(item, priority)

        for i in range(len(self.L)):
            if new_entry.priority < self.L[i].priority:
                self.L.insert(i, new_entry)
                self.len += 1
                return

        self.L.append(new_entry)
        self.len += 1

    def find_min(self):
        if len(self.L) == 0:
            return None

        return self.L[0]

    def remove_min(self):
        if len(self.L) == 0:
            return None

        output = self.L.pop(0)
        self.len -= 1
        return output 



