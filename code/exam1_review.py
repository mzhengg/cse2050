class Node:
    def __init__(self, item, nxt):
        self.item = item
        self.nxt = nxt

class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def add_first(self, item):
        self.head = Node(item, self.head)
        self.len += 1

    def remove_first(self):
        if self.len == 0:
            raise RuntimeError
        else:
            item = self.head.item
            self.head = self.head.nxt
            self.len -= 1
            return item
    
    def add_last(self, item):
        if self.len == 0:
            self.add_first(item)
        elif self.len == 1:
            new_node = Node(item, None)
            self.head.nxt = new_node
            self.len += 1
        else:
            new_node = Node(item, None)
            tail = self.head
            while tail.nxt is not None:
                tail = tail.nxt
            tail.nxt = new_node
            self.len += 1

    def remove_last(self):
        if self.len == 0:
            raise RuntimeError
        elif self.len == 1:
            item = self.head.item
            self.head = None
            self.len -= 1
            return item
        else:
            penult = self.head
            while penult.nxt.nxt is not None:
                penult = penult.nxt
            item = penult.nxt.item
            penult.nxt = None
            self.len -= 1
            return item
            
ll = LinkedList()
for i in range(10):
    ll.add_first(i)
    assert ll.head.item == i
    assert ll.len == i + 1

for i in range(10):
    assert ll.remove_first() == 10-i-1
    assert ll.len == 10-i-1

for i in range(10):
    ll.add_last(i)
    assert ll.len == i + 1

for i in range(10):
    assert ll.remove_last() == 10-i-1
    assert ll.len == 10-i-1

class Node:
    def __init__(self, item, nxt):
        self.item = item
        self.nxt = nxt

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def add_first(self, item):
        if self.len == 0:
            self.head = self.tail = Node(item, None)
            self.len += 1
        elif self.len == 1:
            new_node = Node(item, self.tail)
            self.head = new_node
            self.len += 1
        else:
            new_node = Node(item, self.head)
            self.head = new_node
            self.len += 1

    def remove_first(self):
        if self.len == 0:
            raise RuntimeError
        elif self.len == 1:
            item = self.head.item
            self.head = self.tail = None
            self.len -= 1
            return item
        else:
            item = self.head.item
            self.head = self.head.nxt
            self.len -= 1
            return item

    def add_last(self, item):
        if self.len == 0:
            self.head = self.tail = Node(item, None)
            self.len += 1
        elif self.len == 1:
            new_node = Node(item, None)
            self.head.nxt = new_node
            self.tail = new_node
            self.len += 1
        else:
            new_node = Node(item, None)
            self.tail.nxt = new_node
            self.tail = new_node
            self.len += 1

    def remove_last(self):
        if self.len == 0:
            raise RuntimeError
        elif self.len == 1:
            item = self.head.item
            self.head = self.tail = None
            self.len -= 1
            return item
        else:
            penult = self.head
            while penult.nxt.nxt is not None:
                penult = penult.nxt
            item = penult.nxt.item
            penult.nxt = None
            self.tail = penult
            self.len -= 1
            return item

ll = LinkedList()
for i in range(10):
    ll.add_first(i)
    assert ll.head.item == i
    assert ll.len == i + 1

for i in range(10):
    assert ll.remove_first() == 10-i-1
    assert ll.len == 10-i-1

for i in range(10):
    ll.add_last(i)
    assert ll.len == i + 1

for i in range(10):
    assert ll.remove_last() == 10-i-1
    assert ll.len == 10-i-1

class Node:
    def __init__(self, item, nxt, prev):
        self.item = item
        self.nxt = nxt
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def add_first(self, item):
        if self.len == 0:
            self.head = self.tail = Node(item, None, None)
            self.len += 1
        elif self.len == 1:
            new_node = Node(item, self.tail, None)
            self.tail.prev = new_node
            self.head = new_node
            self.len += 1
        else:
            new_node= Node(item, self.head, None)
            self.head.prev = new_node
            self.head = new_node
            self.len += 1

    def remove_first(self):
        if self.len == 0:
            raise RuntimeError
        elif self.len == 1:
            item = self.head.item
            self.head = self.tail = None
            self.len -= 1
            return item
        else:
            item = self.head.item
            self.head = self.head.nxt
            self.head.prev = None
            self.len -= 1
            return item

    def add_last(self, item):
        if self.len == 0:
            self.head = self.tail = Node(item, None, None)
            self.len += 1
        elif self.len == 1:
            new_node = Node(item, None, self.head)
            self.head.nxt = new_node
            self.tail = new_node
            self.len += 1
        else:
            new_node = Node(item, None, self.tail)
            self.tail.nxt = new_node
            self.tail = new_node
            self.len += 1

    def remove_last(self):
        if self.len == 0:
            raise RuntimeError
        elif self.len == 1:
            item = self.head.item
            self.head = self.tail = None
            self.len -= 1
            return item
        else:
            item = self.tail.item
            self.tail.prev.nxt = None
            self.tail = self.tail.prev
            self.len -= 1
            return item

dl = DoublyLinkedList()
for i in range(10):
    dl.add_first(i)
    assert dl.head.item == i
    assert dl.len == i + 1

for i in range(10):
    assert dl.remove_first() == 10-i-1
    assert dl.len == 10-i-1

for i in range(10):
    dl.add_last(i)
    assert dl.tail.item == i
    assert dl.len == i + 1

for i in range(10):
    assert dl.remove_last() == 10-i-1
    assert dl.len == 10-i-1
