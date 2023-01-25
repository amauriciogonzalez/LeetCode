class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Alternatively, instead of rotating layer by layer, we could also flip the matrix about its
        # anti-diagonal axis and then its horizontal axis to yield an equivalent rotation.

        left = 0
        right = len(matrix) - 1

        while left < right:
            # Iterate through the entire row except the last element
            # to rotate an entire layer.
            # Instead of having (range(left, right + 1)), we use
            # range(right - left) to use i intuitively below.
            for i in range(right - left):
                top = left
                bottom = right

                topLeftStorage = matrix[top][left + i]

                # We rotate a layer clockwise by updating the values counterclockwise.
                # This makes sure that we only need to store one value, the top-left value.
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right] 
                matrix[top + i][right] = topLeftStorage
            
            # Move on to the next layer
            left += 1
            right -= 1
        
        return matrix
