class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root

#size of a tree   
def subtree_size(T):
    def size(u):
        if u == None:
            return 0
        return 1 + size(u.left) +size(u.right)
    return size(T.root)

#print the node at the k level of a tree in-order
def node_at_k(node, k, current_level):
    if node == None:
        return
    node_at_k(node.left, k, current_level + 1)
    if k == current_level:
        print(node.val)
        return
    node_at_k(node.right, k, current_level + 1)

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
    node_at_k(tree.root, 1, 0)

if __name__ == "__main__":
    main()