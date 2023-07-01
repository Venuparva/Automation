def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    totalSum = ""
    resultList = []
    for index, digit in enumerate(digits):
        totalSum = totalSum + str(digit)
        print("totalSum str:%s" % (totalSum))
        if len(digits) - 1 == index:
            result = int(totalSum) + 1
            resultList[:0] = result
            print("result str:%s" % (resultList))
            return resultList
        else:
            print("continue")

plusOne([1,2,3])