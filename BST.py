from TreeNode import TreeNode


class BST():
    def __init__(self):
        self.root = None

    def search(self, val):
        root = self.root
        while(root):
            if val == root.val:
                return root
            root = root.left if val < root.val else root.right

        return root

    def insert_node(self, node, val):
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self.insert_node(node.left, val)
        else:
            node.right = self.insert_node(node.right, val)

        return node

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        self.insert_node(self.root, val)

    @staticmethod
    def replace_node(node1, node2):
        node1.val = node2.val
        node1.left = node2.left
        node1.right = node2.right

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

        return node

    def delete(self,  val):
        self.root = self.delete_node(self.root, val)

    def predecessor(self, node):
        node = node.left
        while(node.right):
            node = node.right

        return node
