from utils import printBTree


class TreeNode():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def printTree(self):
        printBTree(self, lambda n: (str(n.val), n.left, n.right))
