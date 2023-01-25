class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # The O(m * n) memory solution involves making a copy of the matrix.
        # The O(m + n) memory solution involves storing the row and column indicies in
        # two respective 1D arrays which indicate the rows and columns that need to be
        # zeroed out respectively.
        # The O(1) memory solution involves using the same rationale for the O(m + n)
        # memory solution, but using the first row and first column of the matrix itself
        # as an indicator to zero out rows and columns.

        rows = len(matrix)
        cols = len(matrix[0])
        # We need an extra variable to tell us if the first row is zeroed out or not
        # due to the array overlap.
        rowZero = False

        # We determine which rows and columns need to be zeroed out by using the 
        # first row and column of the matrix as a indicators for the future.
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row > 0:
                        matrix[row][0] = 0
                    else: # row == 0
                        rowZero = True
        
        # Zero out the matrix except for the first column and row.
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        
        # If the top left value in the matrix, we zero out the first column.
        if matrix[0][0] == 0:
            for row in range(rows):
                matrix[row][0] = 0
            
        # If the first row needs to be zeroed out, we do it here.
        if rowZero:
            for col in range(cols):
                matrix[0][col] = 0
                
