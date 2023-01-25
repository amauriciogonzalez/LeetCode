class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        instance = []
        def backtrack(numOpen, numClosed):
            if numClosed == numOpen and numClosed == n:
                results.append(''.join(instance))
                return
            if numOpen < n:
                instance.append('(')
                backtrack(numOpen+1, numClosed)
                instance.pop()   
            if numClosed < numOpen:
                instance.append(')')
                backtrack(numOpen, numClosed+1)
                instance.pop()
        backtrack(0,0)
        return results