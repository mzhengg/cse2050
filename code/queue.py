class Queue:
    def __init__(self):
        self._L = []

    def enqueue(self, item):   
        self._L.append(item) # O(1)

    def dequeue(self):
        return self._L.pop(0) # O(n)

if __name__ == '__main__':
    q = Queue()

    n = 10
    for i in range(n):
        q.enqueue(i)

    for i in range(n):
        assert q.dequeue() == i

    print("all done!")

