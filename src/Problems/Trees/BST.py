# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, root=None) -> None:
        self.root = root

    def insert(self, val):
        if root:
            if val < root:
                self.root.left = val
            else:
                self.root.right = val
        else:
            self.root = val

    def inOrderTraversal(self, res):  # Left -->Root--> Right
        res = []
        if self.root:
            res = self.inOrderTraversal(self.root.left, res)
            res.append(root.val)
            res = res + inOrderTraversal(root.right, res)
        else:
            root = root.val


tree = BinaryTree()

root = TreeNode(6)

e1 = tree.insert(5)
e2 = tree.insert(3)
e3 = tree.insert(8)


