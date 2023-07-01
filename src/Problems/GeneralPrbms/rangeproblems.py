from itertools import chain


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        Algm:
        1.Just need to pick 3rd element from all nested lists
        2.add first 2 elements in above results
        """
        elements = [x for x in chain(*grid)]
        print("elements", elements)
        thirdSum = finalSum = 0
        for i in range(2, len(elements), 3):
            print("thirdelement", elements[i])
            thirdSum += elements[i]
            print("thirdsum", thirdSum)

        finalSum = sum(grid[0:1]) + thirdSum

