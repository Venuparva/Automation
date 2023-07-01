from functools import partial
class Node():
    finalTree = [] # Not accessible inside fun(),hence need to pass as args
    def __init__(self,data): # correc-1 : only data arg is needed
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        '''To insert element into BT'''
        # if root is empty
        if self.data: #both self.root == self.data ,no need to declare self.root arg under __init__ fun(),instead use self.data
            # Left side insertion
            if data < self.data: # Check whether incoming data is less than root ( root == data cmp)
                if self.left is None: # ( check left side is empty first)
                    self.left = Node(data) # Need to insert the given element as Node for first time since left side is fully empty
                else:
                    self.left.insert(data) # ( left side Tree is not empty...proceed further )
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

    def printTree(self,finalTree): # self : Need to pass just Node, finalTree: Global declaration not working hence passed as ARGS
        if self.left:
            self.left.printTree(finalTree) #
        finalTree.append(self.data)
        #finalTree += finalTree + str(self.data) + "->"
        if self.right:
            self.right.printTree(finalTree)
        return finalTree

    #In-order Traversal:

    def inOrderTraversal(self,root): # Left-->Root--.Right
        res = []
        if root:
            res = self.inOrderTraversal(root.left) # Left
            res.append(root.data)                  # Root
            res = res + self.inOrderTraversal(root.right) # Right
        return res

    def preOrderTraversal(self,root):
        # res = []
        # if root:
        #     res.append(root.data) # Root
        #     res = res + self.preOrderTraversal(root.left) # Left
        #     res = res + self.preOrderTraversal(root.right) # Root
        # return res
        res = []
        if root:
            res.append(root.data)
            res = res + self.preOrderTraversal(root.left)
            res = res + self.preOrderTraversal(root.right)
        elif root is None:
            return []
        elif root.left is None and root.right is None:
            return res.append(root.data)
        return res

    def postOrderTraversal(self,root):
        res = []
        if root:
            res = res + self.preOrderTraversal(root.left) # Left
            res = res + self.preOrderTraversal(root.right) # Root
            res.append(root.data) # Root
        return res

    def searchnReplace(self,root,findElem,replaceElem):
            if (root == None):
                return False
            if (root.data == findElem):
                root.data = replaceElem
            """ then recur on left subtree """
            res1 = self.searchnReplace(root.left,findElem,replaceElem)
            # node found, no need to look further
            if res1:
                return True
            """ node is not found in left,
            so recur on right subtree """
            res2 = self.searchnReplace(root.right,findElem,replaceElem)
            return res2

    def hasPathSumExists(self, root, sum):
        """ Root to leaf node1+node2+node3 = sum ,if exists,then return TRUE else return FALSE """
        # [3, 4, 6, 8, 5]
        if not root:
            return False
        sum -= root.data # Find the node from root to which their total length == target,once found start reduce 1 by 1 from that node till reach root
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSumExists(root.left, sum) or self.hasPathSumExists(root.right, sum)

    def isheight(self, root):
        "To find which side height is bigger"
        if not root:
            return -1
        return 1 + max(self.isheight(root.left), self.isheight(root.right))


    def treeHeightLeftnRightSide(self,root):
        if root is None:
            return 0
        else:
            leftsideHeight = self.treeHeightLeftnRightSide(root.left)
            print("leftsideHeight",leftsideHeight)
            rightsideHeight = self.treeHeightLeftnRightSide(root.right)
            print("rightsideHeight",rightsideHeight)
        return 1+max(leftsideHeight,rightsideHeight)

    def isBalanced(self, root):
        """ pbm - 110 - balanced binary tree
        To check if tree is balanced -> Left side child nodes height length within 1 ...check LHS height == RHS height (or) RHS height + 1
                3
             9  |   20----> both 9 n 20 at same level
                | 10  25 --> but 10 n 25 at next level -->so height of RHS = 2 level and LHS = 1 ...
                height-diff = RHS - LHS = 2-1 =1 if height-diff < 2 ,then its balanced
        """
        if not root:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and \
               abs(self.isheight(root.left) - self.isheight(root.right)) < 2

root = Node(6)
print("Original Tree-0")
print(root.printTree([]))
root.insert(3)
root.insert(4)
root.insert(8)
root.insert(9)


print("Original Tree")
print(root.printTree([]))
print("In-Order:Left-->Root--.Right")
print(root.inOrderTraversal(root))
print("Pre-Order:Root-->Left-->Right")
print(root.preOrderTraversal(root))
print("Post-Order:Left-->Right->Root")
print(root.postOrderTraversal(root))
#[3,4,8,9,6]
print("searchnReplace:Replace 9 with 5")
root.searchnReplace(root,9,5)
print(root.printTree([]))
print("hasPathSum:total:9")
root.hasPathSumExists(root, 9)
print(root.printTree([]))
print("isBalanced check:",root.isBalanced(root))


#In Order : Left --> Root --> Right

#Pre Order : Root--> Left --> Right

#Post order : Left-->Right-->Root
