class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        outPutList = []
        temp = self.head
        count = 0
        while temp:
            count += 1
            print(temp.data)
            outPutList.append(temp.data)
            temp = temp.next
        print(outPutList)

    def insertAtBeginning(self, newNodeData):
        NewNode = Node(newNodeData)
        print("Inside insertAtBeginning")
        if self.head is None:
            self.head = NewNode
            return  # correction-2 : missed return here
        NewNode.next = self.head
        self.head = NewNode

    def insertAtMiddle(self, oldNode, newNodeData):
        NewNode = Node(newNodeData)
        print("Inside insertAtMiddle")
        if self.head is None:
            self.head = NewNode
            return  # correction-3 : missed return here
        # exit(0)
        NewNode.next = oldNode.next  # Correction-3 It should be oldNode.next
        oldNode.next = NewNode

    def insertAtEnd(self, newNodeData):
        print("Inside insertAtEnd")
        NewNode = Node(newNodeData)
        currNodePtr = self.head
        if self.head is None:
            self.head = NewNode
            return  # forget return here
        while currNodePtr.next:  # Correction-4 : It should be currNodePtr.next not simply currNodePtr..or else it will fail
            currNodePtr = currNodePtr.next
        currNodePtr.next = NewNode

    def listToNode(self, inputList):
        temp = Node(inputList[0])
        i = 0
        while i < len(inputList):
            temp.next = Node(inputList[i])  # Correction-5 - forget type cast here..both correction-4 n 5,(.)NEXT is missing
            temp = temp.next  # Correction -> Totally forget this ptr move
            i += 1
        print(temp)
        return temp


linkedList = SingleLinkedList()
print("started")
e1 = Node(1)
print("node-e1", e1)
linkedList.head = e1  # SELF head declaration - correction-1 ...just e1 is enough no need of e1.data
# Correction-0 : Totally forget to declare remaining nodes and its next ptr
e2 = Node(2)
e3 = Node(3)
# Correction-0 : Totally forget to declare remaining nodes and its next ptr
linkedList.head.next = e2
e2.next = e3
print("linkedList.head", linkedList.head)
linkedList.insertAtBeginning(0)
# linkedList.printList()
linkedList.insertAtMiddle(e1, 5)
linkedList.insertAtEnd(4)
linkedList.printList()