class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        self.
        """
        self.stack = []
        self.minNum = float("inf")
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack) == 0:
            self.minNum = x
            self.minStack.append(x)
        else:
            if x <= self.minStack[-1]:
                self.minNum = x
                self.minStack.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            tmp = self.stack.pop()
            if tmp == self.minNum and self.minStack:
                self.minStack.pop()
                if self.minStack:
                    self.minNum = self.minStack[-1]

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        output = self.stack[-1]
        return output

    def getMin(self):
        """
        :rtype: int
        """
        return self.minNum
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
