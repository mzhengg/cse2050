from BSTNode import BSTNode

# Public interface: users only interact with the class BSTMap.
# Methods in BSTMap often call BSTNode methods, which do the heavy lifting.
class BSTSet:
    def __init__(self):
        self._head = None
        self._len = 0

    def put(self, key):
        if self._head is None:
            self._head = BSTNode(key)
            self._len += 1

        else:
            self._head.put(key)
            self._len += 1

    def __len__(self): return self._len

    def __iter__(self): return iter(self._head)

    def in_order(self): yield from self._head.in_order()

    def pre_order(self): yield from self._head.pre_order()

    def post_order(self): yield from self._head.post_order()

    def __str__(self): pass

if __name__ == '__main__':
    bst = BSTSet()
    n = 4

    # Create a balanced tree with 7 nodes
    #       3
    #    /     \
    #   1       5
    #  / \     / \
    # 0   2   4   6
    for i in [3, 1, 0, 2, 5, 4, 6]: bst.put(i)

    ino = []
    for item in bst.in_order(): ino.append(item)
    assert ino == [0, 1, 2, 3, 4, 5, 6]

    preo = []
    for item in bst.pre_order(): preo.append(item)
    assert preo == [3, 1, 0, 2, 5, 4, 6]

    posto = []
    for item in bst.post_order(): 
        print(item)
        posto.append(item)
    assert posto == [0, 2, 1, 4, 6, 5, 3]

    # unbalanced tree
    # 0
    #  `-1
    #     `-2
    #        `-3
    bst = BSTSet()
    for i in range(n):
        assert len(bst) == i
        bst.put(i)
    print("len works")


    # test in-order
    ino = []
    for key in bst.in_order(): ino.append(key)
    assert ino == [0, 1, 2, 3]
    print("in-order works")

    # test pre-order
    preo = []
    for key in bst.pre_order(): preo.append(key)
    assert preo == [0, 1, 2, 3]
    print("pre-order works")

    # test post-order
    posto = []
    for key in bst.post_order(): posto.append(key)
    assert posto == [3, 2, 1, 0]
    print("post-order works")

    for key in bst:
        print(key)


    
        