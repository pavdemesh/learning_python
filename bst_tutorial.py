"""
Basics: creation and operations on binary search trees
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert_node(self, cursor, value):
        if self.root is None:
            self.root = Node(value)
        else:
            if value < cursor.value:
                if cursor.left is None:
                    cursor.left = Node(value)
                else:
                    self.insert_node(cursor.left, value)
            else:
                if cursor.right is None:
                    cursor.right = Node(value)
                else:
                    self.insert_node(cursor.right, value)
    """I do not understand how to deal with traversing over the bst and how to stop when leaf reached"""
    def visit(self, node):
        if node:
            print(f"node is {node} with value: {node.value}")

    def preorder(self, cursor):
        self.visit(cursor)
        self.preorder(cursor.left)
        self.preorder(cursor.right)


my_tree = BST()
my_tree.insert_node(None, 15)
root = my_tree.root
my_tree.insert_node(root, 12)
my_tree.insert_node(root, 18)
my_tree.insert_node(root, 40)
my_tree.insert_node(root, 13)
my_tree.insert_node(root, 10)

my_tree.preorder(root)

# node1 = Node(15)
# node1.left_child = Node(12)
# node1.right_child = Node(22)
# node1.left_child.left_child = Node(10)
# print(node1.left_child.left_child.left_child)
