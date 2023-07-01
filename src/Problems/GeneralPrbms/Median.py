import math
def findMedian(nums):
    halfLength = len(nums) % 2
    print("halfLength", halfLength)
    if halfLength == 0:
        middle = math.floor(len(nums) / 2)
        print("even list of elements provided", middle)
        #print("sum of elements provided", (nums[middle] + nums[middle-1]))
        medianSum = int(nums[middle] + nums[middle-1])
        print("medianSum value provided", medianSum)
        median = medianSum / 2
        print("median value provided", median)
        return median

findMedian([1,2,3,4])