class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        nonSurrounded = set()

        def dfs(r, c, visited):
            if (r not in range(rows) or
                c not in range(cols) or
                board[r][c] == 'X' or
                (r, c) in visited):
                return
            visited.add((r, c))
            dfs(r + 1, c, visited)
            dfs(r - 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r, c - 1, visited)

        for r in range(rows):
            if board[r][0] == 'O' and (r, 0) not in nonSurrounded:
                dfs(r, 0, nonSurrounded)
            if board[r][cols - 1] == 'O' and (r, cols - 1) not in nonSurrounded:
                dfs(r, cols - 1, nonSurrounded)
        
        for c in range(cols):
            if board[0][c] == 'O' and (0, c) not in nonSurrounded:
                dfs(0, c, nonSurrounded)
            if board[rows - 1][c] == 'O' and (rows - 1, c) not in nonSurrounded:
                dfs(rows - 1, c, nonSurrounded)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in nonSurrounded:
                    board[r][c] = 'X'