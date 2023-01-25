class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        firstNums = [instance[0] for instance in matrix]
        requiredList = 0
        for i in range(1, len(firstNums)):
            if firstNums[i] <= target:
                requiredList = requiredList + 1
            else:
                break
        def search(i, j):
            midpoint = int(float(i + j) / 2)
            if i > j or midpoint >= len(matrix[requiredList]):
                return False
            if matrix[requiredList][midpoint] == target:
                return True
            elif matrix[requiredList][midpoint] < target:
                return search(midpoint + 1, j)
            else:
                return search(i, midpoint - 1)
        return search(0, len(matrix[requiredList]))