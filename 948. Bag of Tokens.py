from collections import deque
class Solution:
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        T = deque(sorted(tokens))
        maxPoints, points = 0, 0
        
        while T and (T[0] <= P or points):
            if T[0] <= P:
                P -= T.popleft()
                points += 1
            else:
                if points >= 1 and T[-1] > P:
                    P += T.pop()
                    points -= 1
            maxPoints = max(maxPoints, points)
        
        return maxPoints
