class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        queue = []
        for i in range(len(s)):
            queue.append(s[i])
            if (len(queue) >= 2):
                if queue[-1] == ')' and queue[-2] != '(':
                    return False
                elif queue[-1] == ')' and queue[-2] == '(':
                    queue.pop()
                    queue.pop()
                elif queue[-1] == ']' and queue[-2] != '[':
                    return False
                elif queue[-1] == ']' and queue[-2] == '[':
                    queue.pop()
                    queue.pop()
                elif queue[-1] == '}' and queue[-2] != '{':
                    return False
                elif queue[-1] == '}' and queue[-2] == '{':
                    queue.pop()
                    queue.pop()
        if not queue:
            return True
        else:
            return False