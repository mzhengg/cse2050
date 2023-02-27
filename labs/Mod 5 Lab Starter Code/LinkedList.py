class Node:
    def __init__(self, _item, _next=None):
        self._item = _item
        self._next = _next

class LinkedList:
    def __init__(self):
        self._head = None
        self._len = 0

    def add_first(self, item):
        # note the ternary (three-parameter) if:
        #    x = a if (boolean) else b
        # equiv to
        #    if (boolean): x = a
        #    else: x = b  
        self._head = Node(item) if (len(self) == 0) else Node(item, self._head)       

        self._len += 1


    def remove_first(self):
        if len(self) == 0: raise RuntimeError("attempt to remove_first from empty LL")

        item = self._head._item         # extract item
        self._head = self._head._next   # cut off head
        self._len -= 1                  # decrease length
        return item                     # return item

    def __len__(self):
        return self._len

    def __str__(self):
        if len(self) == 0: return ''                # edge case - just return an empty string

        list_of_strings = []                        # empty list to hold strings of each item
        self._str(self._head, list_of_strings)      # call helper function _str w/ head node
        return ''.join(list_of_strings)             # join all items in list_of_strings into one string

    # leading underscore - this is private!
    # attributes within this class, like __str__, can call it, but users should not
    # this is called a "helper" function
    def _str(self, node, list_of_strings):
        # base case: tail node
        if node._next is None:
            list_of_strings.append(str(node._item)) # add this item to the list of strings
            return                                  # start bouncing back up chain of recursive calls

        # non-base case: recursively call on next node
        else:
            self._str(node._next, list_of_strings)              # recursively call on next node
        
        # we have hit the tail, and are bouncing back up.
        # add this item to "list_of_strings", then return
        list_of_strings.insert(0, str(node._item) + "-")        # pre-pend "item-" to list of strings

    def __contains__(self, item):
        if self._head == None:
            return False
        else:
            return self._contains(item, self._head)

    def _contains(self, item, node):
        if node == None:
            return False
        elif node._item == item:
            return True
        else:
            return self._contains(item, node._next)

    def add_last(self, item):
        if self._len == 0:
            self.add_first(item)   
        else:
            self._add_last(self._head, item)

    def _add_last(self, node, item):
        if node._next is not None:
            return self._add_last(node._next, item)
        else:
            node._next = Node(item, None)
            self._len += 1

    # TODO: recursive in
    # TODO: recursive add_last

if __name__ == '__main__':
    # Test Node
    n = Node(1)
    assert n._item == 1
    assert n._next is None
    print("Node tests pass")

    # Test LL - add_first/len/remove_first
    LL = LinkedList()
    
    for i in range(4):
        assert len(LL) == i
        LL.add_first(i)
    
    for i in range(4):
        assert LL.remove_first() == 3-i
        assert len(LL) == 3-i

    # Test LL - str
    for i in range(4): LL.add_first(i)
    assert str(LL) == "3-2-1-0"
    print("starter LL tests pass!")

    # Test LL - __in__
    LL_1 = LinkedList()

    assert (0 in LL_1) == False
    for i in range(4):
        LL_1.add_first(i)
        assert i in LL_1
    assert (4 in LL_1) == False
    assert (0 in LL_1) == True

    # Test LL - add_last
    
    LL_2 = LinkedList()
    for i in range(4): 
        LL_2.add_last(i)

    for i in range(4):
        assert LL_2.remove_first() == i
        assert LL_2._len == 4-i-1

    # TODO:
    #   * test in
    #   * test add_last