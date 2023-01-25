class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # O(n * m) and O(1) time and memory complexities, respectively.

        result = []
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        while left < right + 1 and top < bottom + 1:

            # Traverse through the top row of the submatrix
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            # Traverse through the rightmost column of the submatrix
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # This check is necessary for column / row matrices.
            if not (left < right + 1 and top < bottom + 1):
                break

            # Traverse through the bottom row of the submatrix
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

            # Traverse through the leftmost row of the submatrix
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        return result
