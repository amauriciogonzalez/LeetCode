class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Testing the first condition
        for i in range(0, 9, 1):
            rowList = [x for x in board[i] if x != '.']
            if (len(rowList) != len(set(rowList))):
                return False

        # Testing the second condition
        for j in range(0, 9, 1):
            columnList = []
            for i in range(0, 9, 1):
                if board[i][j] != '.':
                    columnList.append(board[i][j])
            print(columnList)
            if (len(columnList) != len(set(columnList))):
                return False

        # Testing the third condition
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                squareList = []
                for k in range(3):
                    squareList = squareList + board[i:i+3][k][j:j+3]
                squareList = [x for x in squareList if x != '.']
                if (len(squareList) != len(set(squareList))):
                    return False
                    
        return True