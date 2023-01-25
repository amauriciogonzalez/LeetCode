class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # In a decision tree, we have len(wordDict) decisions of matching a word
        # to the start of a subproblem in s.
        # So, we have the following:
        # dp[index i of s[i:]] = True / False whether or not s[i:] can be partitioned
        # into words from wordDict. We start with dp[len(s)] = True

        # Time O(len(s)^2 * len(wordDict))

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # If there's enough space for the word to fit into the string
                # and the substring equals the word...
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i] == True:
                    break
        return dp[0]