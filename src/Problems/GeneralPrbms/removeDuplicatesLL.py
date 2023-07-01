def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    {
        1,
        ListNode {
            val: 1,
            next: ListNode {
                val: 2,
                next: None
        }
        }
    }
    """
    prev = head
    # print(head)
    current = head.next
    while current != None:
        print("values before comparison", prev, current)
        if prev.val == current.val:
            print("nodes are equal", prev, current.val)
            # handle both tail & head ptr accordingly
            prev.next = current.next #TAIL ptr handling
            current = current.next # HEAD ptr handling
            print("nodes are equal-2", prev, current)
        else:
            prev = prev.next
            current = current.next
            print("nodes are not equal", prev, current)
        print("continue iterate...", prev, current)
        return
