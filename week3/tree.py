class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root
    
    def pre_order(self, v):
        if v == None:
            return
        print(v.val, end=" ")
        self.pre_order(v.left)
        self.pre_order(v.right)
    
    def post_order(self, v):
        if v == None:
            return
        self.post_order(v.left)
        self.post_order(v.right)
        print(v.val, end=" ")

    def in_order(self, v):
        if v.left != None:
            self.in_order(v.left)
        print(v.val, end=" ")
        if v.right != None:
            self.in_order(v.right)

def main():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = g
    c.right = f
    tree = Tree(a)
    tree.pre_order(tree.root)
    print()
    tree.post_order(tree.root)
    print()
    tree.in_order(tree.root)

if __name__ == "__main__":
    main()      