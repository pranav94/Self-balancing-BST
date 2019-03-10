from BST import BST
from TreeNode import TreeNode
from utils import rotate_left, rotate_right


class Splay(BST):
    def splay(self, root, val):
        if root is None or root.val == val:
            return root

        if root.val > val:
            if root.left is None:
                return root
            if root.left.val > val:
                root.left.left = self.splay(root.left.left, val)
                root = rotate_right(root)
            elif root.left.val < val:
                root.left.right = self.splay(root.left.right, val)
                if root.left.right is not None:
                    root.left = rotate_left(root.left)
            return root if root.left is None else rotate_right(root)
        else:
            if root.right is None:
                return root
            if root.right.val > val:
                root.right.left = self.splay(root.right.left, val)
                if root.right.left is not None:
                    root.right = rotate_right(root.right)
            elif root.right.val < val:
                root.right.right = self.splay(root.right.right, val)
                root = rotate_left(root)
            return root if root.right is None else rotate_left(root)

    def search(self, val):
        self.root = self.splay(self.root, val)
        return super().search(val)


