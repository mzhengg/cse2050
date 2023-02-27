class Stack:
    def __init__(self):
        self._L = [] # list wrapper

    #O(1)
    def push(self, item):
        self._L.append(item)

    #O(1)
    def pop(self):
        return self._L.pop()

    #O(1)
    def __len__(self):
        return len(self._L)

    #O(1)
    def peek(self):
        return self._L[-1]
    
    #O(1)
    def is_empty(self):
        return len(self._L) == 0

if __name__ == '__main__':
    s = Stack()
    n = 10

    assert s.is_empty() == True

    for i in range(n):
        assert len(s) == i
        s.push(i)
        assert s.is_empty() == False
        assert s.peek() == i

    assert len(s) == n

    for i in range(n):
        assert s.pop() == n - 1 - i

    

    print("all done!")