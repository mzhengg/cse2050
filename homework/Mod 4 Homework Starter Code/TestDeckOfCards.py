from DeckOfCards import Node, DoublyLinkedList, DeckOfCards
from CardGenerator import CardGenerator
import unittest

class TestNode(unittest.TestCase):
    def test_init(self):
        node = Node(1, None, None)
        self.assertEqual(node.item, 1)
        self.assertEqual(node.nxt, None)
        self.assertEqual(node.prev, None)

class TestDoublyLinkedList(unittest.TestCase):
    def test_init(self):
        dl = DoublyLinkedList()
        self.assertIsInstance(dl, DoublyLinkedList)
        self.assertEqual(dl.head.item, None)
        self.assertEqual(dl.tail.item, None)
        self.assertEqual(dl.len, 0)

    def test_add_first(self):
        dl = DoublyLinkedList()
        for i in range(10):
            dl.add_first(i)
            self.assertEqual(dl.head.item, i)
            self.assertEqual(dl.len, i+1)
            if i != 0:
                self.assertEqual(dl.head.nxt.item, i-1)
    
    def test_add_last(self):
        dl = DoublyLinkedList()
        for i in range(10):
            dl.add_last(i)
            self.assertEqual(dl.tail.item, i)
            self.assertEqual(dl.len, i+1)
            if i != 0:
                self.assertEqual(dl.tail.prev.item, i-1)

    def test_remove_first(self):
        dl = DoublyLinkedList()
        n = 10
        for i in range(n):
            dl.add_first(i)

        for i in range(n):
            self.assertEqual(dl.remove_first(), n-i-1)
            self.assertEqual(dl.len, n-i-1)

    def test_remove_last(self):
        dl = DoublyLinkedList()
        n = 10
        for i in range(n):
            dl.add_first(i)
        for i in range(0, n):
            self.assertEqual(dl.remove_last(), i)
            self.assertEqual(dl.len, n-i-1)

class TestDeckOfCards(unittest.TestCase):
    def test_init(self):
        cards = CardGenerator()
        my_cards = DeckOfCards(cards)
        self.assertIsInstance(my_cards, DeckOfCards)
        self.assertIsInstance(my_cards.cards, DoublyLinkedList)
        self.assertEqual(my_cards.cards.head.item, cards[-1])
        self.assertEqual(my_cards.cards.tail.item, cards[0])

    def test_deal_top(self):
        my_cards = DeckOfCards([])
        try:
            my_cards.deal_top()
        except RuntimeError:
            pass
        cards = CardGenerator()
        my_cards = DeckOfCards(cards)
        for i in range(len(cards)):
            self.assertEqual(my_cards.deal_top(), cards[-1*(i+1)])
            self.assertEqual(my_cards.cards.len, len(cards) - (i + 1))

    def test_deal_bottom(self):
        my_cards = DeckOfCards([])
        try:
            my_cards.deal_bottom()
        except RuntimeError:
            pass
        cards = CardGenerator()
        my_cards = DeckOfCards(cards)
        for i in range(len(cards)):
            self.assertEqual(my_cards.deal_bottom(), cards[i])
            self.assertEqual(my_cards.cards.len, len(cards) - (i + 1))

    def test_is_cheating(self):
        cards = CardGenerator()
        my_cards = DeckOfCards(cards)
        self.assertEqual(my_cards.is_cheating(cards[-1]), False)
        my_cards.deal_top()
        self.assertEqual(my_cards.is_cheating(cards[-1]), True)
        self.assertEqual(len(my_cards.dict), 1)

unittest.main()