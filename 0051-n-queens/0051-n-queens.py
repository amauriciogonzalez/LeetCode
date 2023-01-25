class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        columns = set()
        # (r + c) We increase column by 1 and decrease row by 1. Positive diagonals are indexed.
        posDiag = set() 
        # (r - c) We increase column by 1 and increase row by 1. Negative diagonals are indexed.
        negDiag = set()
        result = []
        board = [["."] * n for i in range(n)]
        def solveNQueensR(row):
            if row == n:
                copy = ["".join(r) for r in board]
                result.append(copy)
                return
            for col in range(n):
                if col in columns or (row + col) in posDiag or (row - col) in negDiag:
                    continue

                columns.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)
                board[row][col] = "Q"

                solveNQueensR(row + 1)

                columns.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)
                board[row][col] = "."
        solveNQueensR(0)
        return result
