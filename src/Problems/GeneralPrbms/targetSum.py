from typing import List


def findTargetSumWays(nums: List[int], S: int) -> int:
    def dp(start, presum):
        print("inside")
        if start == len(nums):
            return 1 if 0 + presum == S else 0
        return dp(start + 1, presum + nums[start]) + dp(start + 1, presum - nums[start])
    res = dp(0, 0)
    print(res)
    return res

findTargetSumWays([1,0,1,0,1],3)