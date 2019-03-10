from random import randint

from BST import BST
from TreeNode import TreeNode
from utils import rotate_left, rotate_right


class TreapTreeNode(TreeNode):
    def __init__(self, val):
        self.priority = randint(0, 100)
        super().__init__(val)


class Treap(BST):
    def insert_node(self, node, val):
        if node is None:
            return TreapTreeNode(val)

        if val < node.val:
            node.left = self.insert_node(node.left, val)
            if node.left.priority > node.priority:
                node = rotate_right(node)
        else:
            node.right = self.insert_node(node.right, val)
            if node.right.priority > node.priority:
                node = rotate_left(node)

        return node

    def insert(self, val):
        self.root = self.insert_node(self.root, val)

    def delete_node(self, node, val):
        if not node:
            return None
        if val < node.val:
            node.left = self.delete_node(node.left, val)
        elif val > node.val:
            node.right = self.delete_node(node.right, val)
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                if node.right:
                    node.val = node.right.val
                return node.right
            elif not node.right:
                return node.left
            elif node.left.priority < node.right.priority:
                node = rotate_left(node)
                node.left = self.delete_node(node.left, val)
            else:
                node = rotate_right(node)
                node.right = self.delete_node(node.right, val)

        return node

    def delete(self,  val):
        self.root = self.delete_node(self.root, val)
