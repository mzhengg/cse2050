class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

def print_nodes(node):
    if node is None:
        # Base case
        print()
    else:
        # Print the current node
        print('->', node.data, end=' ')
        # Make a recursive call
        print_nodes(node.link)

class LinkedList:
    def __init__(self):
        self._head = None
        # No counter attribute -> __len__ will be implemented recursively

    def add_first(self, item):
        self._head = Node(item, self._head)

    def remove_first(self):
        if self._head is not None:
            item = self._head.data
            self._head = self._head.link
            return item
        else:
            raise RuntimeError('Cannot remove from an empty list.')

    def add_last(self, item):
        if len(self) == 0:
            self.add_first(item)   
        else:
            self.h_add_last(self._head, item)

    def h_add_last(self, node, item):
        if node.link is not None:
            return self.h_add_last(node.link, item)
        else:
            node.link = Node(item, None)

    # For demonstration and debug purposes: Prints all the elements
    def print_all(self):
        # Calls a recursive helper function
        print_nodes(self._head)

    # Returns the length of the linked list
    def __len__(self):
        if self._head is None:
            return 0
        else:
            return self.h_len(self._head, 0)

    def h_len(self, node, l):
        if node.link is None:
            return l+1
        else:
            return self.h_len(node.link, l+1)

    # Sum all the elements in the linked list
    def sum_all(self):
        if len(self) == 0:
            return 0
        else:
            return self.h_sum_all(self._head, 0)

    def h_sum_all(self, node, s):
        if node.link is None:
            return s + node.data
        else:
            s += node.data
            return self.h_sum_all(node.link, s)

    # Create a deep copy: Create a new linked list with all its data copied
    def deep_copy(self):
        LL = LinkedList()
        if len(self) == 0:
            return LL
        else:
            return self.h_deep_copy(self._head, LL)

    def h_deep_copy(self, node, LL):
        if node is not None:
            LL.add_last(node.data)
            return self.h_deep_copy(node.link, LL)
        else:
            return LL

    # Reverses the list in linear time, no copying of the data
    def reverse(self):
        if self._head is None:
            self._head
        else:
            self.h_reverse(self._head)

    def h_reverse(self, node):
        if node.link is None:
            self._head = node
        else:
            self.h_reverse(node.link)
            self.add_last(node.data)



