class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Tree:
    def __init__(self, root):
        self.root = root

"""
中序遍历的下一个节点
    如果有左子节点，返回左子结点
    如果没有左子结点但有右子节点，返回右子节点
    都没有，遍历父结点，一直到找到某个有右节点的节点且其右节点不是node
"""
def pre_order_next(node):
    if node == None:
        return None
    if node.left != None:
        return node.left
    elif node.left == None and node.right != None:
        return node.right
    cursor = node
    while cursor.parent != None:
        if cursor.parent.right != None and cursor.parent.right != node:
            return cursor.parent
        cursor = cursor.parent
    return None #到根结点了还没找到说明是最后一个节点了


"""
中序遍历的下一个节点
    如果有右子节点，返回右子节点的最左子结点
    如果没有，遍历父结点，一直到找到某个节点是其父节点的左节点的节点
"""
def in_order_next(node):
    if node == None:
        return None
    #如果有右子树，则找右子树的最左节点
    if node.right != None:
        node = node.right
        while node.left != None:
            node = node.left
        return node
    #没右子树，则找第一个当前节点是(其父节点的左节点)的节点
    while node.parent != None:
        if node.parent.left == node:
            return node.parent
        node = node.parent
    return None #到根结点了还没找到说明是最后一个节点了


"""
后续遍历的下一个节点
    如果无父结点，已经是最后一个了
    如果是父节点的右节点，下一个节点是父结点
    如果是父结点的左节点且父结点没有右子节点，下一个节点是父结点
    如果是父结点的左节点且父结点有右子节点，返回父结点右子节点的最左子结点
"""
def post_order_next(node):
    if node == None:
        return None
    if node.parent == None:
        return None
    v = node.parent
    if v.right == node:
        return v
    elif v.right == None:
        return v
    node = v.right
    while node.left != None:
        node = node.left
    return node