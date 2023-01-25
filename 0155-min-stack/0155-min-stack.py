class MinStack(object):

    def __init__(self):
        self.stack = []
        self.decStack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.decStack:
            val = min(val, self.decStack[-1])
        self.decStack.append(val)

        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.decStack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.decStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()