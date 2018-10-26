from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tree = defaultdict(list)
        stack, path = ["JFK"], []
        
        for ticket in sorted(tickets):
            tree[ticket[0]].append(ticket[1])
        
        while stack:
            if tree[stack[-1]]:
                stack.append(tree[stack[-1]].pop(0))
            else:
                path.append(stack.pop())
       
        return path[::-1]
