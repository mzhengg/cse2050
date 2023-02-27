from bstMAP_recr_template import BSTNode

class BSTMap:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        if self.root: self.root.put(key, value)
        else: self.root = BSTNode(key, value)

    def get(self, key):
        if self.root: return self.root.get(key).value
        raise KeyError("key {} is not in BSTMap".format(key))

    def floor(self, key):
        if self.root: floor_node = self.root.floor(key)

        if floor_node: return floor_node.key, floor_node.value
        else: return None, None

if __name__ == '__main__':
    bst = BSTMap()
    n = 8

    for i in range(n):
        bst.put(i, str(i))

    for i in range(n):
        assert bst.get(i) == str(i)

    for i in range(1, n):
        assert bst.floor(i-0.1) == ((i-1), str(i-1))
    
    print("all done")
