def backtrackSoln():
    output = []
    tempSubSet = []

    nums = [1,2,3]
    i = 0
    def backtrack(nums,start):
        output.append(nums)
        #i = start
        for i in range(len(nums)):
            tempSubSet.append(nums[i])
            backtrack(tempSubSet,i+1)
            tempSubSet.pop()

    backtrack(nums,0)
    return output

backtrackSoln()
