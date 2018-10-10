from collections import defaultdict
class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        counter = defaultdict(int)
        
        for row in wall:
            edge = 0
            
            for i in range(len(row) - 1):
                edge += row[i]
                counter[edge] += 1
        
        if not counter:
            return len(wall)
        return len(wall) - (max(counter.values()))
