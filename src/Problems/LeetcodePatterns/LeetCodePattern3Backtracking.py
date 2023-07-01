from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    def backtrack(first=0, curr=None):
        # if the combination is done

        if curr is None:
            curr = []
        if len(curr) == k:
            print("not proceed further inside backtrack len:%d k:%d" % (len(curr), k))
            output.append(curr[:])
            print("output",output)
            print("----------")
            return
        else:
            print("proceed further")
        for i in range(first, n): # range(0,3)
            # add nums[i] into the current combination
            print("i=", i)
            print("bef-nums", nums)
            print("bef-curr-iter", curr)
            curr.append(nums[i]) # [1, 2]
            print("aft-curr-iter",curr)
            print("-----new-----")
            # use next integers to complete the combination
            backtrack(i + 1, curr) # 2,[1, 2]
            # backtrack
            curr.pop()

    output = []
    n = len(nums)
    for k in range(n + 1): # range(0,4)
        print("*******")
        print("back to K",k)
        backtrack()
    print("finalo/p",output)
    return output

subsets([1, 2, 3])