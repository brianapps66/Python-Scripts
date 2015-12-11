import sys

class Node:
    def __init__(self, key = 0, value = None, left_child = None,
                 right_child = None, parent = None, colour = None):
        self.key = key
        self.data = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent
        self.colour = colour
    def get_key(self):
        return self.key
    def get_data(self):
        return self.data
    def get_left_child(self):
        #if self.left_child:
            return self.left_child
    def get_right_child(self):
        #if self.right_child:
            return self.right_child
    def get_parent(self):
        return successor(self)
    def get_colour(self):
        return self.colour


class Tree:
    def __init__(self, root):
        self.root = root
    def get_root(self):
        return self.root

"""class NodeTree:
    def __init__(self, left, key, value, right):
        self.left_child = left
        self.key = key
        self. data = value
        self.right_child = right"""

def insert(root, node):
    if root is None:
        root = node
    else:
        if node.get_key() < root.get_key():
            if root.get_left_child() is None:
                root.left_child = node
            else:
                return insert(root.get_left_child(), node)
        else:
            if root.get_right_child() is None:
                root.right_child = node
            else:
                return insert(root.get_right_child(), node)

def insert2(tree, node):
    temp = None
    my_root = tree.root
    while my_root:
        temp = my_root
        if node.key < my_root.key:
            my_root = my_root.left_child
        else:
            my_root = my_root.right_child
    node.parent = temp
    if not temp:
        tree.root = node
    elif node.key < temp.key:
        temp.left_child = node
    else:
        temp.right_child = node


def delete(tree, node):
    if not node.left_child or not node.right_child:
        y = node
    else:
        if node.left_child:
            y = node.left_child
        else:
            y = node.right_child

    if y.left_child:
        x = y.left_child
    else:
        x = y.right_child

    if x:
        x.parent = y.parent

    if not y.parent:
        tree.root = x
    elif y == y.parent.left_child:
        y.parent.left_child = x
    else:
        y.parent.right_child = x

    if y != node:
        node.key = y.key
        node.data = y.data
        node.colour = y.colour

    return y



def tree_min(root):
    while root.left_child:
        root = root.left_child
    return root


def tree_max(root):
    while root.right_child:
        root = root.right_child
    return root

def successor(node):
    if node.right_child:
        #print(node.right_child)
        tree_min(node.right_child)
    y = node.parent
    while y and node == y.right_child:
        node = y
        y = y.parent
    return y


def in_order_traversal(root, callback):
    if not root:
        return
    in_order_traversal(root.get_left_child(), callback)
    callback(root.get_key())
    in_order_traversal(root.get_right_child(), callback)




def iterative_in_order_traversal(root, callback):
    node = root
    stack = []
    while len(stack) != 0 or node != None:
        if node != None:
            stack.append(node)
            node = node.left_child
        else:
            node = stack.pop()
            callback(node.data)
            node = node.right_child



def pre_order_traversal(root, callback):
    if not root:
        return
    callback(root.data)
    pre_order_traversal(root.left_child, callback)
    pre_order_traversal(root.right_child, callback)


def iterative_pre_order_traversal(root, callback):
    stack = []
    stack.append(root)
    if not root:
        return
    while len(stack) != 0:
        node = stack.pop()
        callback(node.data)
        if node.right_child:
            stack.append(node.right_child)
        if node.left_child:
            stack.append(node.left_child)


def post_order_traversal(root, callback):
    if not root:
        return
    post_order_traversal(root.left_child, callback)
    post_order_traversal(root.right_child, callback)
    callback(root.data)


def iterative_post_order_traversal(root, callback):
    node = root
    stack = []
    lastNodeVisited = None
    while len(stack)!= 0 or node != None:
        if node:
            stack.append(node)
            node = node.left_child
        else:
            peekNode = stack[len(stack)-1]
            if peekNode.right_child and lastNodeVisited != peekNode.right_child:
                node = peekNode.right_child
            else:
                callback(peekNode.data)
                lastNodeVisited = stack.pop()



def breadth_first_traversal(root, callback):
    queue = []
    queue.insert(0, root)
    while len(queue) != 0:
        traverse = queue.pop()
        callback(traverse.data)
        if traverse.left_child != None:
            queue.insert(0, traverse.left_child)
        if traverse.right_child != None:
            queue.insert(0, traverse.right_child)


def isBST(root, minKey, maxKey):
    if not root:
        return True
    if root.data < minKey or root.data > maxKey:
        return False
    return isBST(root.left_child, minKey, root.data) and isBST(
        root.right_child, root.data, maxKey)



root = Node(5, "a")
tree = Tree(root)
node = Node(6, "g")
insert2(tree, Node(8, "b"))
insert2(tree, Node(3, "c"))
insert2(tree, Node(7, "d"))
insert2(tree, Node(1, "e"))
insert2(tree, Node(2, "f"))
insert2(tree, node)
insert2(tree, Node(4, "h"))
insert2(tree, Node(9, "i"))
insert2(tree, Node(10, "j"))

delete(tree, node)


"""root2 = Node(1, "a")
tree = Tree(root2)
#print(type(root))
insert2(tree, Node(2, "b"))
insert2(tree, Node(3, "c"))
insert2(tree, Node(4, "d"))
insert2(tree, Node(5, "e"))
insert2(tree, Node(6, "f"))"""


print(root.data)
in_order_traversal(root, print)

#in_order_traversal(root2, print)



"""
             5
      /             \
    3                 8
  /   \             /   \
1       4         7       9
  \             /           \
    2         6               10
"""

#iterative_post_order_traversal(root, print)
#print(isBST(root, -sys.maxsize, sys.maxsize))
