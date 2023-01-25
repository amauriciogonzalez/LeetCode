class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # The mapping below isn't necessary since we are returnning the number of encodings.
        # In this case, we would use a decision tree, which is a brute force approach. O(2^n)
        # for each decision having a max of two next decisions.
        # letterToNum = {
        #    '1' : 'A',
        #    '2' : 'B',
        #    '3' : 'C',
        #    '4' : 'D',
        #    '5' : 'E',
        #    '6' : 'F',
        #    '7' : 'G',
        #    '8' : 'H',
        #    '9' : 'I',
        #    '10' : 'J',
        #    '11' : 'K',
        #    '12' : 'L',
        #    '13' : 'M',
        #    '14' : 'N',
        #    '15' : 'O',
        #    '16' : 'P',
        #    '17' : 'Q',
        #    '18' : 'R',
        #    '19' : 'S',
        #    '20' : 'T',
        #    '21' : 'U',
        #    '22' : 'V',
        #    '23' : 'W',
        #    '24' : 'X',
        #    '25' : 'Y',
        #    '26' : 'Z' 
        #}

        # This is a recursive dynamic programming solution.

        dp = {len(s) : 1}
        def dfs(i):
            if i in dp:
                return dp[i] 
            if s[i] == '0':
                return 0
            result = 0
            result += dfs(i + 1) # Taking i as a single digit.
            if (i + 1 < len(s)) and (s[i] == '1' or (s[i] == '2' and int(s[i+1]) <= 6)):
                result += dfs(i + 2)
            dp[i] = result
            return result
        return dfs(0)

        # This is a bottom-up iterative DP solution.
        """
        if not s:
            return 0
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, len(s) + 1):
            # One digit jump
            if 0 < int(s[i-1]) <= 9:
                dp[i] += dp[i - 1]
            # Two digit jump
            if 10 <= int(s[i-2 : i]) <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]
        """



