'''
#Stack
#From DSA book PDF by Narashimha -> Check Google Drive for this book (Data Structure and Algorithmic Thinking with Python Data Structure and Algorithmic Puzzles ( PDFDrive ))
#Valid paranthesis check

1.Simple data structure to store data
2.Piles of arranged plates in cafeteria is good example -> last placed plate will be taken out first
3.Operations : PUSH + POP ( Always done at one side called "TOP")
4. Exceptions :
    A.PUSH -> Tries to add extra element on top of already full stack
    B.POP -> Tries to remove extra element on top of empty stack
5.Auxillary stack operations :
    1.Top - Returns Last element
    2.size - Returns total size of stack
    3.IsEmptystack - Returns TRUE whether stack is empty
    4.IsFullstack - Returns TRUE whether stack is full
---------------------
Example Algorithms of Stack
---------------------
Direct applications:
---------------------
1.Balancing of symbols
2.Infix-to-postfix conversion
3.Evaluation of postfix conversion
4.Implementing function calls
5.Finding of spans
6.page visited history in web browser
7.Undo sequence in text & editor
8.Matching tags in HTML n XML

---------------------
InDirect applications:
---------------------

1.Auxillary DS for other algorithms ( Exmaple : Tree traversal )
    DFS -> Depth first search
2.Components of other data structure
    Simulating queues
-----------------
Ways of implementation
------------------
1.Simple array based implementation
2.Dynamic ,,    ,,   ,,
3.Linked lists ,, ,, ,,
--------------
1.Simple array based implementation
----------------
Normal way of implement stack using simple array by adding elements on top n removing from top

performance -> O(1) for push,pop,isempty etc operations ...O(n) for N push operations

Limitations : max Size of stack must be defined first (i.e) N = 5 ..we can't increase size for extra elements
--------------
2.Dynamic array based implementation
----------------
We can increase size of stack if needed for extra elements by increasing TOP pointer by 1
by copying all old elements to new Array of extra 1 size added

Ex. Suppose old array with N=3 elements,if user wants to add extra 1 element then he will
increase its size by adding 1 extra eleemnst by creating new Array with size N=4 and then copy all old elements to
new one

performance -> O(n^2) --> Since all old elements to be copied again n again

In order to reduce complexity,would recommend to use Repeated Doubling approach..by increasing its size by double (i.e) N=3*2 = 6
so that Complexity remains O(1) or O(n) in same array without creating new One
-------------
3.Linked List Implementation
-------------
PUSH operation -> Implemented by inserting element at begin of list
POP  ,, -> delete element at begin of list

TOP
  |
| 4 | | -> | 5 | | -> | 6 | | -> | 7 | |-> NULL

Difference between Array n Linked List implementation
--------------------------------------------
Array Implementation           |  LinkedList Implementation
--------------------------------------------
Operations takes constant      |  Each operation takes O(1) time
time

Expensive doubling operation
if needed                     |  It grows + shrink gracefully

Sequence operation -> O(n)    | Uses Extra space + time to deal with references
'''
'''
Problems:
##############
#validate paranthesis
##############
To check whether paranthesis are valid or not
() (()) []
Algorithm :
                    0.REVERSE WAY : Declare dictionary using lookup = {')': '(', '}': '{', ']': '['}
                    1.iterate trough string char by char from input "()[]{}"
                    2.insert first char "("  from input into stack => stack ['(']
                    3.check for second char whether its closing bracket ")" for first element 
                    by doing look up whether its present in lookup DICT (or) not
                    4.if its present,then pop() that element
                    5. check len(stack) == 0 means string is valid
                    6. else string is not valid 
                    7. follow ( [ ? ? ==> logic referred by lee instructor for better ideas
                    #-----------
                    #output below
                    #-----------
                    inputStr = "()[]{}"
                    stack ['(']
                    stack [] -> remove prev above element since incoming close bracket ")" present in lookup and its value matches with this one 
                    stack ['[']
                    stack []
                    stack ['{']
                    stack []
'''
stack = []
lookup = {')': '(', '}': '{', ']': '['}
def validParanthesis(input: str):
    for char in input:
        if char in lookup.values():
            stack.append(char)
        elif stack and lookup[char] == stack[-1]:
            stack.pop()
        print("stack",stack)
    if len(stack) == 0:
        return True
    else:
        return False
inputStr = "()[]{}"
#print(validParanthesis(inputStr))
'''
inputStr = "()[]{}"
stack ['(']
stack []
stack ['[']
stack []
stack ['{']
stack []

'''
#############
# Infix to postfix conversion
#############
#"2+3-4" =>  23+4- ( Infix to postfix conversion)
#Storing all symbols  in stack and charcs to RES variable
    #stack = ["+"]
    #res = 23
#if new next symbol(-) is coming then pop old element from stack
# append to res with 23
#res = 23+ ; stack = []
# Now (-) is coming append to stack = ["-"]
# 4 is coming append to res,repeat the same logic n results in 23+4-
#############
postfixStack = []
res = ''
i = 0
def infixToPostFixConversion(input: str,res):
    global i
    for char in input:
        if not char.isalnum():
            postfixStack.append(char)
        elif char.isalnum():
            res += char
            if len(postfixStack) > 0:
                res += postfixStack[-1]
                postfixStack.pop()
            else:
                print("proceed further")
    print("res",res)
    print("postfixStack", postfixStack)

#infixToPostFixConversion("2+3-4",res)

##########
#palindrome using stack
# Assume input = "madam" and store as GIVEN_STRING
# Iterate through string and push into stack named as reverseStrStack[]
# Iterate reverseStrStack[] using pop operations ..so that it will print elements from backwards
# and store the result as REVERSE_STRING
# if GIVEN_STRING == REVERSE_STRING:
#    then palindrome
# else:
#     not palindrome
##########
#print(infixToPostFixConversion(inputStr))
##########
#Remove recrusive (or) adjacent characters from string
# input = careermonk output = camonk
# input = mississippi output = m

#Algm:
# Insert all elements to stack one by one
# if incoming char is repeated n present in TOP of stack,then pop it and skip that chara
#
###########
output = []
def removeRecursive(inputStr: str):
    for char in inputStr:
        if char not in output:
            output.append(char)
        else:
            output.pop()
    print("Output",output)
    return "".join(output)

#resOut = removeRecursive("mississippi")
#print(resOut)
'''
Problem-7 What is the most appropriate data structure lo print clements ofqueue in reverse order? 
Solution: Stack.

'''

#########
# Replace every elem with nearest greatest elem
'''Input: arr[] = [ 4 , 5 , 2 , 25 ]
Output:  4      –>   5
               5      –>   25
               2      –>   25
              25     –>   -1
              '''
def findNearestNumber(inputNumbers):
    for index in range(len(inputNumbers)):
        print("inputNumbers[index]-before",inputNumbers[index])
        print("------")
        if index == len(inputNumbers)-1:
            inputNumbers[index] = -1
        elif index == 0 and inputNumbers[index] == (max(inputNumbers)):
            print("first index")
            inputNumbers[index] = -1
            print("inputNumbers[index]-after", inputNumbers[index])
        for maxElem in inputNumbers[index+1:]:
            if maxElem > inputNumbers[index]:
                print("next elem is high..update it", maxElem)
                inputNumbers[index] = maxElem
                break
            else:
                print("next elem is low..check further",maxElem)
        #maxValue = max(inputNumbers[index+1:])
        #print("index", index)
        #print("maxValue", maxValue)
        #inputNumbers[index] = maxValue
    print("finalo/p",inputNumbers)
findNearestNumber([ 13 , 7, 6 , 12 ])




