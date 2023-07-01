'''
#########
Queue
########
1.data structure used for storing data (similar to Linked Lists and stacks)

Operations:

Enqueue -> Insert elements at end

Dequeue -> Delete element from front

FIFO -> First IN First Out

Underflow -> try to delete element from empty queue

Overflow -> try to add element in already full queue

 '''
###########
#Problems n Solutions
#2 ways to implement queue using python
# from collections import dequeue
# from queue import Queue
##########
from collections import *
q = deque()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(2)
q.append(5)
print("queue",q) #[1, 2, 3, 4, 2, 5]
q.pop()
print("queue-after-pop",q) # [1, 2, 3, 4, 2]
q.popleft()
print("queue-popleft",q) # [2, 3, 4, 2]

from queue import Queue
r = Queue(maxsize=6)
r.join()
r.put("a")
r.put(2)
r.put("c")

print("new-Q",r)
print("new-Qvalues",r.get())
for item in r.queue:
    print(item)

###############
###Maximum sliding window target sum
##############
# this is possible using double circular Queue ,since addition n deletion allowed on both ends
# (1 3 -1) -3 5 3 6 7
# how do you reverse the order of the first k elements of the queue,
# leaving the other elements in the same relative order?
# Problem - (10, 20, 30, 40, 50, 60, 70, 80, 90) k=4
# O/p = [40, 30, 20, 10,      50, 60, 70, 80, 90].
#
# My solution using list

def partialReverseList(templist,k):
    return sorted(templist[0:k],reverse=True) + templist[k+1:]


