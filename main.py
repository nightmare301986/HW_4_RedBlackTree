
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.color = 1  # 1 for red, 0 for black


class RedBlackTree:
    def __init__(self):
        self.null_node = Node(None)
        self.null_node.color = 0  # set color of null node to black
        self.root = self.null_node

    def insert(self, key):
        new_node = Node(key)
        new_node.left = self.null_node
        new_node.right = self.null_node

        # insert new node as a leaf node
        parent = None
        current = self.root
        while current != self.null_node:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        # rebalance the tree after insertion
        self._rebalance(new_node)

    def _rebalance(self, node):
        while node.parent.color == 1:  # if parent is red
            if node.parent == node.parent.parent.left:  # if parent is left child of grandparent
                uncle = node.parent.parent.right

                if uncle.color == 1:  # case 1: uncle is red
                    node.parent.color = 0
                    uncle.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:  # case 2: uncle is black and node is right child
                        node = node.parent
                        self._left_rotate(node)

                    # case 3: uncle is black and node is left child
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self._right_rotate(node.parent.parent)
            else:  # if parent is right child of grandparent
                uncle = node.parent.parent.left

                if uncle.color == 1:  # case 1: uncle is red
                    node.parent.color = 0
                    uncle.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:  # case 2: uncle is black and node is left child
                        node = node.parent
                        self._right_rotate(node)

                    # case 3: uncle is black and node is right child
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self._left_rotate(node.parent.parent)

        self.root.color = 0

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.null_node:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.null_node:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y
