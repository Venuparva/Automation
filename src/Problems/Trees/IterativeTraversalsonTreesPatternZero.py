class Node():
    def __init__(self, data):  # correc-1 : only data arg is needed
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        '''To insert element into BT'''
        # if root is empty
        if self.data:  # both self.root == self.data ,no need to declare self.root arg under __init__ fun(),instead use self.data
            # Left side insertion
            if data < self.data:  # Check whether incoming data is less than root ( root == data cmp)
                if self.left is None:  # ( check left side is empty first)
                    self.left = Node(data)  # Need to insert the given element as Node for first time since left side is fully empty
                else:
                    self.left.insert(data)  # ( left side Tree is not empty...proceed further )
            # Right side insertion
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        # elif root is not empty
        else:
            # Left side insertion
            print("root insertion")
            self.data = data

    def printTree(self,finalTree):  # self : Need to pass just Node, finalTree: Global declaration not working hence passed as ARGS
        if self.left:
            self.left.printTree(finalTree)  #
        finalTree.append(self.data)
        # finalTree += finalTree + str(self.data) + "->"
        if self.right:
            self.right.printTree(finalTree)
        return finalTree

    # In-order Traversal:

    def inOrderTraversal(self, root):  # Left-->Root--.Right
        res = []
        if root:
            res = self.inOrderTraversal(root.left)  # Left
            res.append(root.data)  # Root
            res = res + self.inOrderTraversal(root.right)  # Right
        return res

root = Node(6)
print("Original Tree-0")
print(root.printTree([]))
root.insert(3)
root.insert(4)
root.insert(8)
root.insert(9)
print("Original Tree")
print(root.printTree([]))
