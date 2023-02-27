class Node:
    def __init__(self, item = None, nxt = None, prev = None):
        self.item = item
        self.nxt = nxt
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.len = 0

    def add_first(self, item):
        if self.len == 0: # When the list is empty, the head and tail node is the same
            self.head = self.tail = Node(item, None, None)
            self.len += 1
        elif self.len == 1: # When the len(list) is 1, update the head node to the new node and update the tail's prev to this new node
            new_node = Node(item, self.tail, None)
            self.tail.prev = new_node
            self.head = new_node
            self.len += 1
        else: # When len(list) > 1, the tail node is unaffected, just simply update the head node.
            new_node = Node(item, self.head, None)
            self.head.prev = new_node
            self.head = new_node
            self.len += 1

    def add_last(self, item):
        if self.len == 0: # When the list is empty, the tail and the head node is the same
            self.tail = self.head = Node(item, None, None)
            self.len += 1
        elif self.len == 1: # When the len(list) is 1, update the tail node to this new node and update the head's next to this new node
            new_node = Node(item, None, self.head)
            self.head.nxt = new_node
            self.tail = new_node
            self.len += 1
        else:
            new_node = Node(item, None, self.tail)
            self.tail.next = new_node
            self.tail = new_node
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
            new_head = self.head.nxt
            new_head.prev = None
            self.head = new_head
            self.len -= 1
            return item

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
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.len -= 1
            return item

class DeckOfCards:
    def __init__(self, cards = []):
        self.cards = DoublyLinkedList()
        for card in cards:
            self.cards.add_first(card)
        self.dict = {}

    def deal_top(self):
        try:
            card = self.cards.remove_first()
            self.dict[card] = '1'
            return card
        except RuntimeError:
            raise RuntimeError

    def deal_bottom(self):
        try:
            card = self.cards.remove_last()
            self.dict[card] = '1'
            return card
        except RuntimeError:
            raise RuntimeError

    def is_cheating(self, card):
        if card in self.dict:
            return True
        else:
            return False