class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class AE:
    #print在subtree中是左 中 右，所以使用in_order
    def print_expr(self, v):
        if v.left != None:
            print("(", end="")
            self.print_expr(v.left)
        print(v.val,end="")
        if v.right != None:
            self.print_expr(v.right)
            print(")", end="")
    

    #eval需要求出subtree左右的值，最后通过中间连接，所以post_order
    def eval_expr(self, v):
        if v.right is None and v.left is None:
            return int(v.val)
        x = self.eval_expr(v.left)
        y = self.eval_expr(v.right)
        if v.val == "x":
            return x * y
        if v.val == "+":
            return x + y
        if v.val == "-":
            return x - y


def main():
    a = Node("+")
    b = Node("x")
    c = Node("x")
    d = Node("2")
    e = Node("-")
    f = Node("5")
    g = Node("1")
    h = Node("3")
    i = Node("2")
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = f
    e.right = g
    c.left = h
    c.right = i
    ae = AE()
    ae.print_expr(a)
    print()
    print(ae.eval_expr(a))

if __name__ == "__main__":
    main()  