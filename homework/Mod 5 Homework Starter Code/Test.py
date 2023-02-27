import unittest
from LinkedList import LinkedList
from base_conversion import convert_to_base

class TestLinkedList(unittest.TestCase):
    def test_len(self):
        LL = LinkedList()
        for i in range(4):
            LL.add_first(i)
        assert len(LL) == 4

    def test_sum_all(self):
        LL = LinkedList()
        for i in range(4):
            LL.add_first(i)
        assert LL.sum_all() == 6

    def test_deep_copy(self):
        LL1 = LinkedList()
        for i in range(4):
            LL1.add_first(i)
        LL2 = LL1.deep_copy()
        LL1.print_all()
        LL2.print_all()

    def test_reverse(self):
        LL = LinkedList()
        for i in range(10):
            LL.add_first(i)
        LL.print_all()
        LL.reverse()
        LL.print_all()

unittest.main()