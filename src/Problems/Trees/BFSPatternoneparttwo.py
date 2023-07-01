
from collections import deque

class Node(object):
    def __init__(self, data):  # correc-1 : only data arg is needed
        self.left = None
        self.right = None
        self.data = data

    def levelOrder(self,root):
        q = deque()
        if (root != None):
            q.append(root)
        levels = []
        while (len(q) != 0):
            level= []
            lenq = len(q)
            for i in range(lenq):
                temp = q.popleft() # 8 is getting popped,same time its kids are pushed into queue
                if(temp.left != None):
                    q.append(temp.left) #
                if (temp.right != None):
                    q.append(temp.right)
                level.append(temp.data) # Node data append
            print("level", level)
            levels.append(level) # Node level append
        print("levels",levels)
        return levels

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

root = Node(7)

root.insert(8)

root.insert(9)

root.insert(10)

root.insert(11)

root.insert(12)

root.printTree([])

root.levelOrder(root)



