class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listToNode(self, resList):
        '''To find length of the list --> set both head = tail = L[0]=>first element; keep typecast Node() of all other elements'''
        e = 0
        head = Node(resList[0])  # Make both head & tail points to same node first -> head = L[0]=>first element=tail ;
        tail = head  # head = tail = L[0]
        while e < len(resList):  # Iterate continuously till length of list and move tail pointer
            print(head)
            tail.next = Node(resList[e])  #
            tail = tail.next
            e += 1
        return tail

    # TO find length of list
    def len_link(self):
        '''To find length of the list --> one temp ptr ..start from first to last node n increase counter
        temp = head
        temp -> temp.next until temp is None
        '''
        temp = self.headval  # store first head value to temp --> list.headval = Node("Mon")
        count = 0
        while (temp):
            count += 1
            temp = temp.nextval  # continue iteration n make ptr points to next node
        print("count", count)
        return count

    # printing all elements in list
    def listprint(self, listOut=""):
        '''To find length of the list --> set both head = tail = L[0]=>first element; keep typecast Node() of all other elements
        #same as len of linkedlist
        temp = head
        temp -> temp.next until temp is None
        #extra : just add  storing result values to List[] and then print it out
        L = [].append(temp.dataval)
        '''
        temp = self.headval
        count = 0
        while temp:  # Here iterating until headVal (i.e) NodeVal is None
            count += 1
            listOut += temp.dataval + "->"
            temp = temp.nextval
        print(listOut.rstrip("->"))
        print("count", count)

    #Both start n end logic
    # -----------------
    # Beginning logic
    # -----------------
    # 1.create NewNode for incoming value (int)
    # 2.if head = null,then assign to head n return ( empty list case)
    #    3. Ptr handling -->just 2 steps to change ptr like NewNode.next -->self.head -->newNode
    #       a. Newnode.next --> self.head # set TAIL ptr
    #       b. self.head --> NewNode # set HEAD ptr
    #
    #   2 --> 3
    #         ^
    #         |
    #   2 --> 3
    #   ^
    #   |
    # -----------------
    # End logic:
    #-----------------
    # same steps as Begin logic until step-2
    # follow print_list() logic to find last element ptr stop once reaches final node
    # set current.next ->newnode only TAIL PTR handling since adding elem at the end
    # -----------------
    # Middle logic : Same as Begin logic and use oldnode instead of using self.head ...2 params needs to be passed
    # -----------------

    def InsertAtBeginning(self, newNodeData):
        # Create New node first
        # NewNode = |  | Sun |  |
        NewNode = Node(newNodeData)

        # Assume LinkedList is empty,if yes please add this new one element and return it
        if self.headval is None:
            self.headval = NewNode
            return
        # (TAIL POINTER HANDLING) Make nextValptr to current first element = |  | Sun |  |--nextVal ptr-->|  | Mon |  |
        NewNode.nextval = self.headval
        # (HEAD POINTER HANDLING) Make headVal points to New Node first = headVal --> |  | Sun |  |--nextVal ptr-->|  | Mon |  |
        self.headval = NewNode

    # Insert at End
    def InsertAtEnd(self, newNodeData):
        # Create New node first
        # LastNode = |  | Thurs |  |
        NewNode = Node(newNodeData)
        # Assume LinkedList is empty,if yes please add this new one element and return it
        if self.headval is None:
            self.headval = NewNode
            return
        # Pick the current pointer position
        # (HEAD POINTER HANDLING) --headval ptr-->|  | Sun |  |--nextVal ptr-->
        currElementPtr = self.headval
        # Keep move the currentHeadPtr until it reaches the last element
        while (currElementPtr.nextval):
            currElementPtr = currElementPtr.nextval
        # At this level,currentHeadPtr moved to last element
        # (TAIL POINTER HANDLING )
        currElementPtr.nextval = NewNode

    # Insert at Middle
    def InsertAtMiddle(self, middleNodeData, newNodeData):
        if middleNodeData is None:
            print("Middle node is not null")
            return
        # Create New node first
        NewNode = Node(newNodeData)
        # Always recommended to complete TAIL POINTER HANDLING first and then add HEAD POINTER HANDLING
        NewNode.nextval = middleNodeData.nextval
        middleNodeData.nextval = NewNode


# # Initialize the first 3 nodes
# list = SLinkedList()
# list.headval = Node("Mon") # first Node
# e2 = Node("Tue") # second Node
# e3 = Node("Wed") # third Node
#
# # Link first Node to second node
# list.headval.nextval = e2
# # Link second Node to third node
# e2.nextval = e3
#
# list.listprint()
# print("before add")
# #list.InsertAtBeginning("Sun")
# #print("--------")
# print("after last add")
# list.InsertAtEnd("Thurs")
# print("--------")
#
# list.listprint()

list = SLinkedList()
list.headval = Node("Mon") #Learning
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

list.InsertAtMiddle(e3, "Thurs")
list.InsertAtEnd("Fri")

list.listprint()

list.len_link()

print("List to Node conversion:", list.listToNode([1, 2, 3, 4, 5]))
