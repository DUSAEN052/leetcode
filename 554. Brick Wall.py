from collections import Counter
class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        tracker = []
        
        for row in wall:
            edge = 0
            
            for i in range(len(row) - 1):
                edge += row[i]
                tracker.append(edge)
        
        if not tracker:
            return len(wall)
        return len(wall) - (max(Counter(tracker).values()))
