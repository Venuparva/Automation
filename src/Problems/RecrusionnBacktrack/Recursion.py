
'''
-----------
Recursion:
-----------
From DSA book PDF by Narashimha -> Check google drive for this book (Data Structure and Algorithmic Thinking with Python Data Structure and Algorithmic Puzzles ( PDFDrive ))

1.Terminates when a base case is reached.
2.Each recursive call requires extra space on the stack frame (memory).
3.If we gel infinite recursion, the program may run out of memory and result in stack overflow. 
Solutions to some problems use easier to formulate recursively.

There are 2 types of recursion:

1. BASE CASE : Every recursion must terminate at base case

2. RECURSIVE CASE :
    A recursive function performs a task in part by calling itself 
    to perform the subtasks (i.e) where thc function calls itself to pcrform a subtask, 
    is referred to as the cursive case.
    --------
    Format:
    --------
    if(test for the base case)
        return some base case value
    else if(test for another base case)
        return some other base case value
        // the recursive case 
    else
        return (some work and then a recursive call)
#################
https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/tutorial/
#################
Receursion:

Base Case: Any recursive method must have a terminating condition. Terminating condition is one for which the answer is already known and we just need to return that. For example for the factorial problem, we know that , so when  is 0 we simply return 1, otherwise we break into smaller problem i.e. find factorial of . If we don't include a Base Case, the function will keep calling itself, and ultimately will result in stack overflow. For example, the  function given above has no base case. If you write a code for it in any language, it will give a runtime error.

Number of Recursive calls: There is an upper limit to the number of recursive calls that can be made. To prevent this make sure that your base case is reached before stack size limit exceeds.

So, if we want to solve a problem using recursion, then we need to make sure that:

The problem can be broken down into smaller problems of same type.
Problem has some base case(s).
Base case is reached before the stack size limit exceeds.
#################
-----------
Iteration:
-----------
• Terminates when a condition is proven lo be false.
• Each iteration docs not require extra space.
• An infinite loop could loop forever since there is no extra memory being created.
• Iterative solutions to a problem may not always be as obvious as a recursive solution.

----------------------
Example Algorithms of Recursion
----------------------
1.Fibonacci Series, Factorial Finding
2.Merge Sort, Quick Sort
3.Binary Search
4.Tree Traversals and many Tree Problems: 
    lnOrder, 
    PrcOrder 
    PostOrdcr 
5.Graph Traversals: 
        ----------------------
        |                     |
DFS !Depth First Search! + BFS !Breadth First Search!
 
6.Dynamic Programming Examples
7.Divide and Conquer Algorithms 
8.Towers of Hanoi
9.Backtracking Algorithms
'''
#8.Towers of Hanoi
'''
--------
Algorithm:
--------
0.Given disks positions
1. Move the top (n - 1) disks from Source to Auxiliary tower,
2. Move the nth disk from Source to Destination tower,
3. Move the (n - 1) disks from Auxiliary tower to Destination tower.
4. Transferring the top (n - 1) disks from Source to Auxiliary tower can again be thought of as a fresh
problem and can be solved in the same manner. Once we solve Towers of Hanoi with three disks, 
we can solve it with any number of disks with the above algorithm.
-------
Step(0): Given disks position
-------
   |                    |              |
 --|-- (n-1)            |              |
---|--- (n)             |              |
---------          ----------    -----------
Source             Destination   Auxiliary
-------
Step(1): Move the top (n - 1) disks from Source to Auxiliary tower,
-------
   |                    |              |
   |                    |              |
---|--- (n)             |        -|- (n-1)
---------          ----------    -----------
Source             Destination   Auxiliary
-------
Step(2): Move the nth disk from Source to Destination tower,
-------

   |                    |              |
   |                    |              |
   |                 ---|--- (n)      -|- (n-1)
---------          ----------    -----------
Source             Destination   Auxiliary

-------
Step(3): Move the (n - 1) disks from Auxiliary tower to Destination tower.
-------

   |                    |              |
   |                   -|- (n-1)       |
   |                 ---|--- (n)       |
---------          ----------    -----------
Source             Destination   Auxiliary


'''
def TowerofHanoi(numOfDisks,startPeg=1,endPeg=3):
    if numOfDisks:
        TowerofHanoi(numOfDisks - 1, startPeg, 6-startPeg-endPeg) # base Case
        print("Move disk %d from peg %d to peg %d" %(numOfDisks,startPeg,endPeg))
        print("----------")
        TowerofHanoi(numOfDisks - 1, 6-startPeg-endPeg, endPeg) # another base Case

TowerofHanoi(numOfDisks=3)

#******simple recursion***
def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return n*factorial(n-1)
res = factorial(5)
print("res",res)

def IsArrayInSortedOrder(nums):
    if len(nums) == 1:
        return True
    return  nums[0]<=nums[1] and IsArrayInSortedOrder(nums[1:])

A= [127, 220, 246, 277, 321, 454, 534, 565, 933]
print(IsArrayInSortedOrder(A))

