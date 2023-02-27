class Node:
    def __init__(self, _item, _next):
        self._item = _item # whatever item
        self._next = _next # node or None

    def __str__(self):
        if self._next is not None:
            return "Node(item = {}, next._item = {})".format(self._item, self._next._item)
        else:
            return "Node(item = {}, next._item = None)".format(self._item)

class LinkedList:
    def __init__(self):
        self._head = None
        self._len = 0

    def add_first(self, item):
        new_node = Node(item, self._head) # create a new node
        self._head = new_node             # update the LL head
        self._len += 1                    # update length

    def __len__(self):
        return self._len

    def remove_last(self):
        # Edge case: LL is empty
        if len(self) == 0:
            raise IndexError("Cannot remove from empty linked list")

        # Edge case: LL has only item
        if len(self) == 1:
            item = self._head._item # retrieve item
            self._head = None       # cut off tail (tail is head in this case)
            self._len -= 1          # update length
            return item             # return item

        # "Typical" case: LL has 2+ items
        # find penultimate (second to last) node of LL
        penult = self._head
        while penult._next._next is not None:
            penult = penult._next

        item = penult._next._item # retrieve data
        penult._next = None       # cut off tail
        self._len -= 1            # update length
        return item               # return item

    def add_last(self, item):
        # Edge case: empty LL
        if len(self) == 0:
            return self.add_first(item)

        # "Typical" case: 1+ nodes
        # find tail
        tail = self._head
        while tail._next is not None:
            tail = tail._next

        tail._next = Node(item, None)
        self._len += 1

    def remove_first(self):
        # Edge case: empty LL
        if len(self) == 0:
            raise IndexError("You cannot remove from empty LL")

        # Typical case: 1+ nodes
        item = self._head._item # extract data
        self._head = self._head._next # cut off head
        self._len -= 1 # update length
        return item # return item

if __name__ == '__main__':
    ll = LinkedList()
    n = 10
    
    for i in range(n): 
        print("ll._head = {}".format(ll._head))
        ll.add_first(i)

    print()

    for i in range(n):
        print("ll._head = {}".format(ll._head))
        assert ll.remove_last() == i
    print("ll.head = {}".format(ll._head))

    print()

    ll = LinkedList()

    for i in range(n): 
        print("ll._head = {}".format(ll._head))
        ll.add_last(i)
    
#   for i in range(n): 
#       assert ll.remove_last() == n - 1 - i

    for i in range(n):
        assert ll.remove_first() == i

    
