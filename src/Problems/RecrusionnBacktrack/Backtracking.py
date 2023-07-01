
'''

From DSA book PDF by Narashimha

Backtracking is a rorm or recursion.The usual scenario is that you ore focecl with a number (or) options,
and you must choose one or these. After you make your choice you will get a new set of options;
just what set of options you get depends on what choice you made.

This procedure is repeated over and over until you reach a final state.
If you made a good sequence of choices, your final state is a goal state; if you didn't, it isn't.
----------------------
IMPORTANT : Backtracking is a method of exhaustive search using divide and conquer.
----------------------
• Sometimes the best algorithm for a problem is to try all possibilities.
• This is always slow, but there are standard tools that can be used to help.
• Tools: algorithms for generating basic objects, such as
    - binary strings [2^n possibilities for n-bit string],
    - permutations - n!
    - combinations - n!/(n- r)!r!
    - general strings k-array strings or length n has k^n possibilities!. etc...

• Backtracking speeds the exhaustive search by pruning.

One more useful doc:

Backtracking:

So, while solving a problem using recursion, we break the given problem into smaller ones.

Let's say we have a problem, and we divided it into three smaller problems ,
and . Now it may be the case that the solution to  does not depend on all the three subproblems,
in fact we don't even know on which one it depends.

Let's take a situation. Suppose you are standing in front of three tunnels,
one of which is having a bag of gold at its end, but you don't know which one.

Tunnel-1 : check it whether gold is there or not,if not, go back and try tunnel-2
Tunnel-2 : check it whether gold is there or not ,if not, go back and try tunnel-3
Tunnel-3 : check it whether gold is there or not,found the gold finally

So you'll try all three. First go in tunnel , if that is not the one, then come out of it, and go into tunnel ,
and again if that is not the one, come out of it and go into tunnel .

So basically in backtracking we attempt solving a subproblem,
and if we don't reach the desired solution, then undo whatever we did for solving that subproblem, and try solving another subproblem.

---------------------
Example Algorithms of Backtracking
---------------------
• Binary Strings: generating all binary strings
• Generating k -ary Strings
• The Knapsack Problem
• Generalized Strings
• Hamiltonian Cycles [ refer Graphs chapter ]
• Graph Coloring Problem
'''

#Prbms: Generate all the binary strings with n bits. Assume A[O.. n - 1] is an array of size n.
def appendAtbeginingFront(k,n,L):
    print("---------")
    print("current n-value", n)  # 0 ;
    print("X-value",k) # 0 ;
    print("L-value", L) # ['0','1'] ;
    if n == 0:
        return []
    if n == 1:
        return ["0","1"]
    sumVal = [k+element for element in L] # ['00', '01'] ;
    print("sumVal", sumVal)
    return sumVal

def bitStrings(x,n):
    print("0-range started", n)
    if n == 0:
        return []
    #if n == 1:
    #    return ["0","1"]
    else:
        output1 = bitStrings(x,n - 1)
        print("output1  from bitStrings", output1)
        res1 = appendAtbeginingFront(x, n, output1)
        print("res-1 from appendAtbeginingFront o/p", res1)
        #return res1
        # iteration calls for prev line like below
        # appendAtbeginingFront("0", bitStrings(4 - 1)) => appendAtbeginingFront("0", bitStrings(3))
        # appendAtbeginingFront("0", bitStrings(3 - 1)) => appendAtbeginingFront("0", bitStrings(2))
        # appendAtbeginingFront("0", bitStrings(2 - 1)) => appendAtbeginingFront("0", bitStrings(1)) => first o/p returned ['0','1']
        print("1-range started", n)
        output2 = bitStrings(x,n - 1)
        print("output2  from bitStrings", output2)

        res2 = appendAtbeginingFront(x, n, output2)
        print("res-2", res2)
        return res1+res2


finalres1 = bitStrings("0",2)
print("finalres1",finalres1)
#print("############NEW START########")
'''
[]
[0,1]
[00,01] => [0+0,0+1]
[000,001] => [0+00,0+01]
'''
#finalres2 = bitStrings("1",3)
'''
[]
[0,1]
[10,11] => [1+0,1+1]
[110,111] => [1+10,1+11]
'''
#print("finalres2",finalres2)

#print("overall o/p",finalres1+finalres2)

#Difference between Backtracking n recursion

#Recursion

def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return n*factorial(n-1)

#Backtracking

def bitStringsNew(n):
    global temp, digit
    print("n-Val",n)
    if n == 0:
        return []
    if n == 1:
        return ["O", "1"]
    print("bitStringsNew(1)",bitStringsNew(1))
    print("bitStringsNew(n-1)",bitStringsNew(n-1))
    print("--------")
    for digit in bitStringsNew(1):
        print("digit",digit)
        for bitString in bitStringsNew(n-1):
            print("bitString", bitString)
            digit = digit+bitString
    return digit

#newres = bitStringsNew(3)
#print("bitStringsNew-o/p",newres)


def appendAtbeginingFrontNewOne(x,n,L):
    if n == 0:
        return []
    if n == 1:
        return ["0","1"]
    sumVal = [x+element for element in L] # ['00', '01'] ;
    print("sumVal", sumVal)
    return sumVal

def bitStringsNewOne(n):
    print("0-range started", n)
    if n == 0:
        return []
    #if n == 1:
    #    return ["0","1"]
    else:
        res1 = appendAtbeginingFrontNewOne("0", n, bitStringsNewOne(n-1))
        res2 = appendAtbeginingFrontNewOne("1", n, bitStringsNewOne(n-1))
        print("res-", res1+res2)
        return res1+res2

temp = bitStringsNewOne(3)
print("temp",temp)

