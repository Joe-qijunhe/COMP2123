class Queue:
    def __init__(self,N=10):
        self.n = 0
        self.start = 0
        self.Q = [None] * N
    
    def size(self):
        return self.n
    
    def is_empty(self):
        return self.n == 0

    def enqueue(self, e):
        if self.n == len(self.Q):
            raise MemoryError("Queue full")
        end = (self.start + self.n) % len(self.Q)
        self.Q[end] = e
        self.n += 1
    
    def dequeue(self):
        if self.is_empty():
            raise MemoryError("Empty queue")
        e = self.Q[self.start]
        self.Q[self.start] = None
        self.start = (self.start + 1) % len(self.Q)
        self.n = self.n - 1
        return e

    def __str__(self):
        return str(self.Q)

def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q)
    q.dequeue()
    print(q)

if __name__ == "__main__":
    main()   