def permute(nums):
    result = []

    if(len(nums) == 1):
        return [nums[:]]

    for i in range(len(nums)):
        print("1-nums",nums)
        n = nums.pop(0)
        print("2-n",n)
        perms = permute(nums)
        print("3-perms",perms)
        for perm in perms:
            perm.append(n)
        result.extend(perms)
        print("4-result",result)
        print("-----------")
        nums.append(n)

    return result

permute([1,2,3])
