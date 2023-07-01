from typing import List
#pbm-1 : Generate binary strings with n bits say n = 3
def appendAtBeginningFront(x, L):
    return [x + element for element in L]

def bitStrings(n):
    if n == 0: return [] # Base condition-1
    if n == 1: return ["0","1"] # Base condition-2
    return (appendAtBeginningFront("O", bitStrings(n-1)) + appendAtBeginningFront("1", bitStrings(n-1))) # Recursive condition

#print(bitStrings(2)) # ['OO0', 'OO1', 'O10', 'O11', '1O0', '1O1', '110', '111']
#--------------------------------------
#pbm-2 : Generate all the strings of length n drawn from 0... k - 1...following same logic given in pbm-1..just add "2" in n == 1 n also in recursive call
def appendAtBeginningFront(x, L):
    return [x + element for element in L]

def SubSetsAlter(n):
    if n == 0: return [] # Base condition-1
    if n == 1: return ["0","1","2"] # Base condition-2 # Change-1 adding extra values
    return (appendAtBeginningFront("O", SubSetsAlter(n-1)) + appendAtBeginningFront("1", SubSetsAlter(n-1)) + appendAtBeginningFront("2", SubSetsAlter(n-1))) # Recursive condition # Change-2 adding extra values for "2" here

SubSets = SubSetsAlter(2)
print("SubSets-Append",SubSets) # ['O0', 'O1', 'O2', '10', '11', '12', '20', '21', '22']

#Alternative Soln without hard code values

def baseKStrings(n,k):
    global result
    if n == 0: return n # range - 0 handled here
    if n == 1: return [str(x)  for x in range(0,k)] # range - 1 handled here # [0,1,2]
    return [digit+bitstring for digit in baseKStrings(1,k) for bitstring in baseKStrings(n-1,k)]
    #[ outerVariable + innervariable outerloop innerloop]# nothing but below one
    '''    
          for digit in baseKStrings(1, k):
              for bitstring in baseKStrings(n-1, k): # range - 1 to K handled here
                  result += [digit + bitstring]
    '''


#print(baseKStrings(1,3)) # [0,1,2]
print(baseKStrings(2,3)) # ['O0', 'O1', 'O2', '10', '11', '12', '20', '21', '22']
#print(baseKStrings(3,3))

'''
['0', '1', '2']
['00', '01', '02', '10', '11', '12', '20', '21', '22']
['000', '001', '002', '010', '011', '012', '020', '021', '022', 
'100', '101', '102', '110', '111', '112', '120', '121', '122', 
'200', '201', '202', '210', '211', '212', '220', '221', '222']

'''

def subsetsNewOne(nums):
    output = [[]]
    nums.sort()
    #temp = [[]] + [s+[nums[i]] for i in range(len(nums)) for s in subsetsNewOne(nums[:i])]
    for i in range(len(nums)):#[1][2][3]
        for s in subsetsNewOne(nums[:i]):#nums[:0]=[],nums[:1]=[1],nums[:2]=[1,2],nums[:3]=[1,2,3],
            val = s + [nums[i]] # [1] + 2 = [1,2] ; [1] + 3 = [1,3] ; [1, 2] + 3 = [1,2,3]
            print("val", val) # [1,2] ; [1,3]
            output.append(val)
    return output # without this one,it will throw None type error

subsetsNewOne([1,2,3])

#subsets([1, 2, 3]) # [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

#Alternative solution below

def subsets(nums: List[int]) -> List[List[int]]:
    def backtrack(first=0, curr=None):
        if curr is None: # 2nd iter - 1,[1] ; 4th iter - > curr = 1,[1]
            curr = [] # 1st iter -> curr = []
        if len(curr) == k: # 1st iter -> k= 0 # k= 1 => [[], [1], [2], [3] ; k = 2 => [[], [1], [2], [3], [1, 2], [1, 3]] ; k= 3 => [1,2,3] will be added
            output.append(curr[:]) # 1st iter -> output = [[]] ; 2nd iter -> output = [[],[1]] ...
            return
        for i in range(first, n): # range(0,3)=> 0,1,2
            curr.append(nums[i]) # 1st iter -> won't reach here ; 2nd iter - > curr = [1]  ; 3rd iter - > curr = [2] ; 4th iter - > curr = [1] ; 5th iter [1, 2] ; 6th iter [1, 3]
            backtrack(i + 1, curr) # 1st iter -> won't reach here ; 2nd iter - > 1,[1] ; 3rd iter - > curr = 2,[2] ; 4th iter - > curr = 3,[3] ; 5th iter 2, [1, 2] ; 6th iter 3, [1, 3] ;  8th iteration 3, [2,3]
            curr.pop() # [[1]] ;; 5th iter 2, [1, 2] #pop-last eleme-2,hence [1] for next iteration ; 7ith iteration pop-element [1] from curr ; 8th iteration [2,3]

    output = []
    n = len(nums)
    for k in range(n + 1): # range(0,4)
        print("*******")
        print("back to K",k) # At end of k = 1,o/p is [[], [1], [2], [3] ; At end of k = 2,o/p is [[], [1], [2], [3], [1, 2], [1, 3], [2, 3]]
        backtrack()
    print("finalo/p",output)
    return output

#subsets([1, 2, 3]) # [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]



'''#########
## 39. Combination Sum
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.'''
#########
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    results = []

    def backtrack(remain, comb, start):
        if remain == 0:
            # make a deep copy of the current combination
            results.append(list(comb))
            return
        elif remain < 0:
            # exceed the scope, stop exploration.
            return

        for i in range(start, len(candidates)):
            # add the number into the combination
            comb.append(candidates[i])
            # give the current number another chance, rather than moving on
            backtrack(remain - candidates[i], comb, i)
            # backtrack, remove the number from the combination
            comb.pop()

    backtrack(target, [], 0)

    return results

#########
# 46 - permutation using backtracking   Leetcode solution code using simple PYTHON swap variables logic
#########
def permute(nums):
    def backtrack(first=0):
        if first == n:
            output.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first] # same logic is repeated
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]  # # backtrack - same logic is repeated

    n = len(nums)
    output = []
    backtrack()
    print("permute-o/p",output)
    return output

#########same problem with more logging
# 46 - permutation using backtracking   Leetcode solution code using simple PYTHON swap variables logic
#########
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    def backtrack(first=0):
        # if all integers are used up
        if first == n:
            print("first", first)
            print("n", n)
            output.append(nums[:])
            print("output-now",output)
        for i in range(first, n):
            # place i-th integer first in the current permutation
            print("-------")
            print("inside loop i",i)
            print("first inside loop", nums[i])
            print("nums[i]", nums[i])
            print("before-nums",nums)
            print("before nums[first]", nums[first])
            print("before-nums[i]", nums[i])
            nums[first], nums[i] = nums[i], nums[first] # same logic is repeated
            # use next integers to complete the permutations
            print("after-nums-1", nums)
            print("after nums[first]", nums[first])
            print("after-nums[i]", nums[i])
            backtrack(first + 1)
            print("after-nums-2", nums)
            # backtrack
            nums[first], nums[i] = nums[i], nums[first]  # same logic is repeated again

    n = len(nums)
    output = []
    backtrack()
    print("permute-o/p",output)
    return output

#permute(['a','b','c']) #[['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a'], ['c', 'b', 'a'], ['c', 'a', 'b']]
#permute([1,2,3]) # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]