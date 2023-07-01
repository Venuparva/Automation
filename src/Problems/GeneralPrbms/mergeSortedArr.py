def sort(nums1, m, nums2, n):
    if m == 1:
        return nums1
    elif n == 1:
        return nums2
    else:
        res = nums1 + nums2
        res = list(filter(lambda a: a != 0, res))
        finallist = sorted(res, reverse=False)
        print("finallist:", finallist)
    return finallist


resfinal = sort([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
print("resfinal",resfinal)
