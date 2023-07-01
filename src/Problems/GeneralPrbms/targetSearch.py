# from typing import List
#
#
# def searchInsert(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: int
#     """
#     # boundary cases
#     if target < nums[0] and nums[0] - target > 1:
#         difference = nums[0] - target
#         return 0
#     for index, value in enumerate(nums):
#         if value == target:
#             print("straight forward")
#             return index
#         elif len(nums) - 1 == index:
#             print("element not found")
#             if target + 1 in nums:
#                 if target + 1 == nums[0]:
#                     print("element not found but first elem:target+1:%s" % (nums.index(target + 1)))
#                     return 0
#                 else:
#                     print("element not found:target+1:%s" % (nums.index(target + 1)))
#                     return nums.index(target + 1)
#             elif target - 1 in nums:
#                 if target - 1 == nums[-1]:
#                     print("element not found but last elem:target-1:%s" % (nums.index(target - 1)))
#                     return len(nums)
#                 else:
#                     print("element not found:target-1:%s" % (nums.index(target - 1)))
#                     return nums.index(target - 1)
#             else:
#                 print("list is empty")
#                 return -1
#         else:
#             print("continue search...")
#
#
# searchInsert([2, 3, 4, 8, 10], 0)


def twoSum():
    resultListIndex = []
    nums = [3, 2, 3]
    target = 6
    x = y = sum = 0

    if len(nums) < 1:
        return resultListIndex
    elif len(nums) == 2:
        if nums[0] + nums[1] == target:
            return [0, 1]
    else:
        print("some other comb..proceed further")

    for index in range(len(nums)):
        y = target - nums[index]
        print("iterate:%d" % y)
        if y in nums:
            yindex = nums.index(y)
            xindex = index
            print("y:%d:x:%d:x-index:%d:yindex:%d:xindex:%d" % (y, nums[index], index, yindex, xindex))
            print("yindex:%d:xindex:%d" % (yindex, xindex))
            if yindex != xindex:
                print("both x n y index are not equal")
                print("y:%d:%d:%d" % (y, index, nums.index(y)))
                resultListIndex.append(index)
                resultListIndex.append(nums.index(y))
                return resultListIndex
            else:
                print("both x n y index are equal")
        elif len(nums) - 1 == index:
            print("no matching target found")
            return []
        else:
            print("continue iterate...")

twoSum()