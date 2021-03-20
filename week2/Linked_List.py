class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.n = 0
    
    def size(self):
        return self.n
    
    def is_empty(self):
        return self.n == 0

    def first(self):
        return self.head
    
    def insert_first(self, e):
        self.head = Node(e, self.head)
        self.n += 1
    
    def remove_first(self):
        if self.is_empty():
            raise RuntimeError("empty")
        e = self.head.val
        self.head = self.head.next
        self.n -= 1
        return e

    def insert_before(self, p, e):
        if self.is_empty():
            raise RuntimeError("empty")
        x = Node(e, p)
        cursor = self.head
        while(cursor.next != None):
            if cursor.next == p:
                cursor.next = x
                return
        raise RuntimeError("can not find")
    
    def __str__(self):
        cursor = self.head
        result = ""
        while (cursor != None):
            result += str(cursor.val)
            if cursor.next != None:
                result += "->"
            cursor = cursor.next
        return result

def main():
    list = LinkedList()
    list.insert_first(1)
    list.insert_first(2)
    list.remove_first()
    

if __name__ == "__main__":
    main()      