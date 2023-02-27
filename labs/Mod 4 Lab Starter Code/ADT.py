from LinkedList import LinkedList

class Stack_L:
    def __init__(self): 
        self._L = list()  # Composition: the Stack_L class has a List
    
    def push(self, val):
        self._L.append(val)
        
    def pop(self):
        return self._L.pop() 

class Stack_LL:
    def __init__(self):
        self._LL = LinkedList() # Composition: the Stack_LL class has a Linked List
        
    
    def push(self, val):
        self._LL.add_first(val)
        
    def pop(self):
        return self._LL.remove_first()

class Queue_L:
    def __init__(self):
        self._Q = list()

    def enqueue(self, item):
        self._Q.insert(0, item)

    def dequeue(self):
        return self._Q.pop()

class Queue_LL:
    def __init__(self):
        self._Q = LinkedList()

    def enqueue(self, item):
        self._Q.add_last(item)

    def dequeue(self):
        return self._Q.remove_first()

if __name__ == '__main__':
    ##########Test Stack_L##########
    s1 = Stack_L()

    for i in range(10): s1.push(i*3)

    for i in range(9,-1,-1): assert(s1.pop() == i*3)

    ##########Test Stack_LL#########
    s1 = Stack_LL()

    for i in range(10): s1.push(i * 92)

    for i in range(9, -1, -1): assert s1.pop() == i * 92

    ##########Test Queue_L##########
    q1 = Queue_L()

    for i in range(10): q1.enqueue(i * 73)

    for i in range(10): assert q1.dequeue() == (i * 73)

    ##########Test Queue_LL#########
    q1 = Queue_LL()
    
    for i in range(10): q1.enqueue(i)

    for i in range(10): assert q1.dequeue() == i

    print("Everything works!")