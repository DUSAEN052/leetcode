class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        
        while pushed:
            stack.append(pushed.pop(0))
            
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)

        return stack == popped[::-1]
