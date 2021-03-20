class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def __str__(self):
        return str(self.val)

def reverse_list(head):
    last = None
    for i in range(0,3):
        cursor = head
        while cursor.next != last:
            cursor = cursor.next
        print(cursor, end=" ")
        last = cursor

x = Node('1')
y = Node('2')
z = Node('3')
x.next = y
y.next= z
reverse_list(x)
