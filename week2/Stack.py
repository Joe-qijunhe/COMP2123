class Stack:
    def __init__(self, N=10):
        self.n = 0
        self.S = [None] * N
    
    def size(self):
        return self.n
    
    def is_empty(self):
        return self.n == 0
    
    def pop(self):
        if self.is_empty():
            return None
        self.n -= 1
        item = self.S[self.n]
        self.S[self.n] = None 
        return item

    def push(self, e):
        if self.n == len(self.S):
            raise MemoryError("Stack overflow")
        self.S[self.n] = e
        self.n += 1
    
    def first(self):
        return self.S[self.n - 1]

    def __str__(self):
        return str(self.S[:self.n])
def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack)
    stack.pop()
    print(stack)

if __name__ == "__main__":
    main()      