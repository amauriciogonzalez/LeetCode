class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        result = 0
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                result = stack.pop() + stack.pop()
                stack = stack + [result]
            elif tokens[i] == '-':
                a = stack.pop()
                b = stack.pop()
                result = b - a
                stack = stack + [result]
            elif tokens[i] == '*':
                result = stack.pop() * stack.pop()
                stack = stack + [result]
            elif tokens[i] == '/':
                a = stack.pop()
                b = stack.pop()
                result = int(float(b) / a)
                stack = stack + [result]
            else:
                stack.append(int(tokens[i]))
        return stack[0]