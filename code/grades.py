class Entry:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __hash__(self):
        return hash(self.name)

        # Classes enable hasing by default but if we define equality
        # python disables hasing and we have to define our own hash function
        # because the built-in hash function doesn't know what equality means anymore
        # and guarantee consistency for same objects


    def __eq__(self, other):
        # It is important to define equality this way
        # Otherwise we could have the same person with a different grade
        # and we would have 2 keys with seperate values and that would
        # not work
        # General rule: we only hash the keys
        return self.name == other.name

    def __repr__(self):
        return f"Entry(name={self.name}, grade={self.grade})"

class GradeMapping:
    def __init__(self):
        self.n_buckets = 10
        self.L = [[] for i in range(self.n_buckets)]
        self.len = 0

    def add_grade(self, name, grade):
        new_entry = Entry(name, grade)

        bucket = hash(new_entry) % self.n_buckets

        for entry in self.L[bucket]:
            if new_entry == entry:
                entry.grade = grade # update the person's grade if they are already in the list
                                    # len is not update here because they are already in the list we are just updating the value

        self.L[bucket].append(new_entry) # if they are not in the buckets already, add them and their grade in.
        self.len += 1 # update the len since it is a new entry

    def __contains__(self, name):
        new_entry = Entry(name)

        bucket = hash(new_entry) % self.n_buckets

        for entry in self.L[bucket]:
            if new_entry == entry:
                return True

        return False

if __name__ == '__main__':
    import random
    names = {"Ax", "Cassie", "Jake", "Marco", "Rachel", "Tobias"}
    gm = GradeMapping()
    for name in names:
        gm.add_grade(Entry(name, random.gauss(75, 10)))
        assert name in gm

    # Two foundational hashing requirements:
    # 1) Should get the same hash every time I has the same object
    # 2) Should get the same hash every time I hash equal objects

