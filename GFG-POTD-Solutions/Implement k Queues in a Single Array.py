class kQueues:

    def __init__(self, n, k):
        # Initialize your data members
        self.n=n
        self.k=k
        self.arr=[0] * n
        self.front=[-1] * k
        self.rear = [-1] * k
        self.next = list(range(1,n)) + [-1]
        self.free = 0

    def enqueue(self, x, i):
        # Enqueue element x into queue number i
        if self.free == -1:
            return
        idx = self.free
        self.free = self.next[idx]
        if self.front[i] == -1:
            self.front[i] = idx
        else:
            self.next[self.rear[i]] = idx
        self.next[idx] = -1
        self.rear[i] = idx
        self.arr[idx] = x

    def dequeue(self, i):
        # Dequeue element from queue number i
        if self.front[i] == -1:
            return -1
        idx = self.front[i]
        self.front[i] = self.next[idx]
        
        self.next[idx] = self.free
        self.free=idx
        if self.front[i] == -1:
            self.rear[i] = -1
        return self.arr[idx]

    def isEmpty(self, i):
        # Check if queue i is empty
        return self.front[i] == -1
        
    def isFull(self):
        # Check if array is full
        return self.free == -1