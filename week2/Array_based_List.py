class Array:
    def __init__(self, n=10):
        self.n = 0
        self.capacity = n
        self.A = [None] * self.capacity
    
    def size(self):
        return self.n
    
    def get(self, i):
        if i < 0 or i >= self.n:
            raise IndexError("index out of bound") 
        else:
            return self.A[i]

    def set(self, i , e):
        if i < 0 or i >= self.n:
            raise IndexError("index out of bound") 
        self.A[i] = e

    def add(self, i, e):
        if self.n == self.capacity:
            raise MemoryError("array is full")
        if i < 0 or i > self.n:
            raise IndexError("index out of bound") 
        for j in range(self.n-1, i-1, -1):
            self.A[j+1] = self.A[j]
        self.A[i] = e
        self.n += 1

    def remove(self, i):
        if i < 0 or i >= self.n:
            raise IndexError("index out of bound")
        e = self.A[i]
        for j in range(i, self.n-1):
            self.A[j] = self.A[j+1]
        self.n -= 1
        return e 

    def __str__(self):
        return self.A[:self.n].__str__()


def main():
    arr = Array()
    arr.add(0,1)
    print(arr)


if __name__ == "__main__":
    main()      