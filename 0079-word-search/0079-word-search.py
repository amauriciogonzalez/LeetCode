class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        path = set() # we use a set of positions to make sure we don't reuse the same letter cell
        def existR(r, c, index):
            if index == len(word):
                return True
            # Out of bounds or wrong character or the same position was visited
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                word[index] != board[r][c] or
                (r, c) in path):
                return False
            path.add((r, c))
            # Look at all four adjacent positions
            result = (existR(r + 1, c, index + 1) or
                      existR(r - 1, c, index + 1) or 
                      existR(r, c + 1, index + 1) or
                      existR(r, c - 1, index + 1))
            path.remove((r,c))
            return result

        # Brute force the root of the search in the whole board
        for r in range(rows):
            for c in range(cols):
                if existR(r, c, 0):
                    return True
        return False
        
        # O(n * m * existR) = O(n * m * 4^len(word)) for four positions to visit