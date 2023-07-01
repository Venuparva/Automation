from typing import List

#
# def permute(num: List[int]) -> List[List[int]]:
#
#     n = len(num)
#     ans = []
#
#     def solve(nums, j):
#         print("------")
#         print(nums,j)
#         if j == n:
#             ans.append(nums[:])
#
#         for i in range(j, n):
#             nums[i], nums[j] = nums[j], nums[i]
#             print("before nums-1:%s:j:%d"%(nums,j))
#             solve(nums, j + 1)
#             nums[i], nums[j] = nums[j], nums[i]
#             print("after nums-1", nums)
#
#     solve(num, 0)
#     print(ans)
#    return ans

#permute([1,2,3])

def backtrack(d, visited, ans, nums):
    print("------")
    print("visited", visited)
    print("ans", ans)
    print("nums",nums)
    print("d", d)

    if len(d) == len(nums):
        ans.append(d.copy())
        print("append n return",d)
        return

    for i in range(len(nums)):
        print("before-i",i)
        if not visited[i]:
            d.append(nums[i])
            visited[i] = True
            print("calling backtrace")
            backtrack(d, visited, ans, nums)
            print("back from backtrace")
            print("after-i", i)
            d.pop()
            visited[i] = False
    return ans

nums = [1,2,3]
visited = [0] * len(nums)
d, ans = [], []
res = backtrack(d, visited, ans, nums)
print("res",res)