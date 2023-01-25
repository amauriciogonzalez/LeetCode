class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numToLetter = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz",
        }
        result = []
        def letterCombinationsR(string, index):
            if len(string) == len(digits):
                result.append(string)
                return
            for c in numToLetter[digits[index]]:
                string = string + c
                letterCombinationsR(string, index + 1)
                string = string[:-1]
            
        if digits:
            letterCombinationsR("", 0)
        return result