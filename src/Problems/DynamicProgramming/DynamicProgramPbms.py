'''

Introduction:

1.Dynamic Programming (DP) is a simple technique, but it can be difficult to master.
2.One easy way to identify and solve DP problems is by solving as many problems as possible.
3.The term Programming is not related to coding, but it is from literature, and
means filling tables (similar to linear Programming).
-----------
DP strategy:
-----------

Dynamic programming and memoization work together. The main difference between dynamic programming and
divide and conquer is that in the case of the latter, sub problems are independent,
whereas in DP there can be an overlap of sub problems.

By using memoization !maintaining a table of sub problems already solved,
dynamic programming reduces lhe exponential complexity to polynomial complexity (0(112), 0(11:1), etc.) for many problems.

--------------
The major components of DP are:
--------------

• Recursion: Solves sub problems recursively.
• Memoization: Stores already computed values in table (Memoization means caching).
-----------
Properties of DP strategy:
-----------
The two dynamic programming properties which can tell whether il can solve the given problem or nol arc:
• Optimal substructure: an optimal solution to a problem contains optimal solutions to sub problems.
• Overlappingsubproblems: a recursive solution contains a small number of distinct sub problems
repeated many times.
-----------
Can Dynamic Programming Solve All Problems?
-----------
Like Greedy and Divide and Conquer techniques, DP cannot solve every problem. There arc problems which
cannol be solved by a ny a lgorithmic technique [Greedy, Divide and Conquer a nd Dyna mic Programming!.

Answer : No,it can't solve all problems
-----------
Difference between DP and Recursion:
-----------
1.Main difference is memoization of recursive calls

2.if sub problems are independent and there is no repetition then memoization does not help,
so dynamic programming is not a solution for all problems.

-----------
DP Approaches:
-----------

1.Bottom Up DP

2.Top Down DP

-----------
Bottom Up DP approach:
-----------

1.Start with small input arg and process it and store its result in table

2.slowly increase input arg values to higher value,re-use above smaller values during higher-value processing

-------------
Ex: Find  fibonacci upto 5
-------------

fib(5)
fib(4) + fib(3) --> cumulative additions of these smaller values  helps in forming above higher value
(fib(3) + (fib(2)) + (fib(2) + fib(1)) --> cumulative additions of these smaller values  helps in forming above higher values
((fib(2) + fib(l)) + (fib(1) + fib(O))) + ((fib(l) + fib(O)) + fib(1))
(((fib(l) + (fib(O)) + fib(1)) + (fib(1) + fib(O))) + ((fib(1) + fib(O)) + fib(1))

-----------
Top Down approach:
-----------

1.Problem will be broken into sub-problems and its respective solutions are remembered which will be used for future purpose

First Action : Check whether sub-problem solution already exists

Final Action : Store the result of sub-problem solution n use it for future operations


Note: Some problems can be solved with both the techniques

-------------
Ex: Find  fibonacci upto 5 --> need to add solution using Top-down approach
-------------

--------------------------
Examples of Dynamic Programming Algorithms
--------------------------

• String algorithms:
    longest common subsequence,
    longest increasing subsequence,
    longest common substring,
    edit distance.
• Algorithms on graphs can be solved efficiently:
    Bcllman- Pord a lgorithm for finding the shortest distance in a graph,
    Floyd's All-Pairs shortest path algorithm, etc.
• Chain matrix multiplication
• Subset Sum
• 0/ I Knapsack
• Travelling salesman problem, and many more
'''

#Understanding DP with examples
#Fibonacci prbm:
#Fib(n) =0,                     for n =0
#       =1,                     for n=1
#       =Fib(n- 1)+Fib(n- 2)    for n > 1

#---------------
# Soln : using Simple recursive call
#---------------
def Fibo(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fibo(n- 1)+Fibo(n-2)
print (Fibo(5))

'''---------------
# Alternative Soln using Simple recursive call bottom Up approach
#How does Memoization help?
#Calling fib(S) produces a cull tree that calls the function on the same value many times:
fib(5)
fib(4) + fib(3)
(fib(3) + (fib(2)) + (fib(2) + fib(1))
((fib(2) + fib(l)) + (fib(1) + fib(O))) + ((fib(1) + fib(O)) + fib(1))
(((fib(1) + (fib(O)) + fib(1)) + (fib(1) + fib(O))) + ((fib(1) + fib(O)) + fib(1))

In the above example, (fib(2) was calculated three times (overlapping of subproblems).
If n is big, then many more values of fib (sub problems) are recalculated, which leads to an exponential lime algorithm. 
Instead of solving the same sub problems again and again we can store the previous calculated values 
and reduce the complexity.
-----------
Memoization works like this: 
-----------
Start with a recursive function and add a table that maps the function's parameter values 
to the results computed by the function. 
-----------
table:
-----------
fib(0) | 1
fib(1) | 1
fib(2) | 2
fib(3) } 6
 
Then if this function is called twice with the same parameters, we simply look up the answer in the table

#---------------'''
#---------------
# Soln : using Simple recursive call
#---------------
def Fibo(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fibo(n- 1)+Fibo(n-2)
print (Fibo(5))
#---------------
# Alternative Soln : using BOTTOM UP APPROACH
#---------------
def Fibo(n):
    fibTable = [0, 1]
    for i in range(2,n+1):
        fibTable.append(fibTable[i-1] + fibTable[i-2])
        return fibTable[n]
#print(Fibo(5))
#---------------
# Alternative Soln : using TOP DOWN APPROACH
#---------------
fibTable= {1:1,2:1} # Storing the results with input args
def Fibo(n):
    if n <= 2: return 1
    if n in fibTable:
        return fibTable[n]
    else:
        fibTable[n] = Fibo(n-1) + Fibo(n-2)
        return fibTable[n]
#print(Fibo(5))
#IMPORTANT : For all problems, it may not be possible to find both top-down and bottom-up programming solutions.
#---------------
# Further Improving:
#---------------
# One more observation from the Fibonacci series is:
# The current value is the sum of the previous two calculations only.
# This indicates that we don't have to store all the previous values.
# Instead, if we store just the last two values, we can calculate the current value.
#---------------
def Fibo(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        return a
#print(Fibo(5))
'''
---------------
Observations:
---------------
While solving the problems using DP, try to figure out the following:
• See how the problems are defined in terms of subproblems recursively.
• See if we can use some table [memoization] to avoid the repeated calculations.

another example : factorial
'''
#---------
# using recursive approach
#---------
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)
#print(factorial(6))
#---------
# using DP approach
#---------
factTable = {}
def factorial(n):
    try:
        return factTable[n]
    except KeyError:
        if n == 0:
            factTable[0] = 1
            return 1
        else:
            factTable[n] = n * factorial(n-1)  # store the previously calculated result in table
            return factTable[n]
#print(factorial(10))

'''
Problem -4 Maximum Value Contiguous Subsequence: 
Given an array of N numbers, give an algorithm for finding A substring A(i)...A(j) for 
which the sum of elements is maximum
------
Example:
------
[-2,11,-4,13,-5,2] = 20 ( 11-4+13 )
[I,-3,4,-2,-1,6] = 7 ( 4-2-1+6 )
'''
def MaxContigousSum(A):
    # A = [-2,11,-4,13,-5,2]
    n = len(A)
    M = [0] * (n+1)
    ##############
    #Initialize M List with all values as zero and set only first value from input array if its greater than zero ; else no change
    print("M values-1",M) # [0, 0, 0, 0, 0, 0, 0]
    if A[0] > 0:
        M[0] = A[0] # suppose if A = [3,11,-4,13,-5,2] given with first positive number 3 instead of -2 ,then A[0] = 3,then M[0] = 3
    else:
        M[0] = 0 # Needed since A[0] = -2 ,hence else becomes true and add M[0] = 0, [0, 0, 0, 0, 0, 0, 0]
    print("M values-2", M) # [0, 0, 0, 0, 0, 0, 0] if A[0] = -2 ,else [3, 0, 0, 0, 0, 0, 0] if A[0] = 3
    ##############
    for i in range(1, n):
        print("-------")
        print("M[i-1]",M[i-1]) # m[1-1] => M[0] => 0
        print("A[i]", A[i]) # A[1] = 11
        if(M[i-1] + A[i] > 0): # 0 + 11=11 ; 11-4=7; 7+13=20; 20-5=15; 15+2 = 17 ( note that its using previously calculated values using DP concept)
            M[i] = M[i-1] + A[i] # [0, 11, 0, 0, 0, 0, 0] ; [0, 11, 7, 0, 0, 0, 0] ; [0, 11, 7, 20, 0, 0, 0]... [0, 11, 7, 20, 15, 17, 0]
        else:
            M[i] = 0
        print("M values-3", M)
    print("maxSum", max(M))
    return max(M)

A= [-2,11,-4,13,-5,2]
MaxContigousSum(A)
'''
M(i) = Max( M(i-1) + A[i], 0)
'''