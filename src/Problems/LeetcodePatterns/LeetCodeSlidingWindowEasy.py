import sys
from typing import List



def minSubArrayLen(target: int, nums: List[int]) -> int:
    sum=nums[0]
    minSize= sys.maxsize
    begin,end=0,0
    while end<len(nums) and begin<len(nums):
        print(begin,end)
        if sum<target:
            end=end+1
            if end==len(nums): break
            sum=sum+nums[end]
            range = nums[begin:end+1]
            print("less range",range)
            print("less range-sum", sum)
        elif sum>=target:
            range = nums[begin:end+1]
            print("more range-1",range)
            print("more range-before-sum", sum)
            newsize = end-begin+1
            if newsize<minSize:
                minSize=newsize
                print("minSize",minSize)
            sum=sum-nums[begin]
            begin=begin+1
            print("ranges:begin:%d:end:%d"%(begin,newsize+1))
            range = nums[begin:newsize+1]
            print("more range-2", range)
            print("more range-after-sum", sum)
            print("move-begin-after-range", begin)
        print("-------")
    return 0 if minSize== sys.maxsize else minSize

minSubArrayLen(7,[2,3,1,2,4,3])


