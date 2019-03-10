from BST import BST
from TreeNode import TreeNode


class AVLTreeNode(TreeNode):
    def __init__(self, val):
        self.height = 0
        super().__init__(val)


class AVL(BST):
    def rotate_left(self, node):
        new_root = node.right
        left_tree_of_new_root = new_root.left
        new_root.left = node
        node.right = left_tree_of_new_root

        self.calculate_height(node)
        self.calculate_height(new_root)
        return new_root

    def rotate_right(self, node):
        new_root = node.left
        right_tree_of_new_root = new_root.right
        new_root.right = node
        node.left = right_tree_of_new_root

        self.calculate_height(node)
        self.calculate_height(new_root)
        return new_root

    def rebalance(self, node):
        b = self.balance(node)
        if b > 1:
            if self.balance(node.left) >= 0:
                return self.rotate_right(node)
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if b < -1:
            if self.balance(node.right) <= 0:
                return self.rotate_left(node)
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert_node(self, node, val):
        if not node:
            return AVLTreeNode(val)

        if val < node.val:
            node.left = self.insert_node(node.left, val)
        else:
            node.right = self.insert_node(node.right, val)

        self.calculate_height(node)

        return self.rebalance(node)

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
            else:
                x = self.predecessor(node)
                t = x.val
                node.left = self.delete_node(node.left, t)
                node.val = t

        self.calculate_height(node)
        return self.rebalance(node)

    def delete(self,  val):
        self.root = self.delete_node(self.root, val)

    def calculate_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    @staticmethod
    def height(node):
        if not node:
            return 0

        return node.height

    def balance(self, node):
        if not node:
            return 0

        return self.height(node.left) - self.height(node.right)
