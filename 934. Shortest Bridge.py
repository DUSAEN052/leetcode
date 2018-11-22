from collections import deque
class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def border(section, x, y):
            if x == 0 or x == len(section) - 1 or y == 0 or y == len(section[0]) - 1:
                return False
            return section[x + 1][y] and section[x - 1][y] and section[x][y + 1] and section[x][y - 1]
        
        def flood(section, x, y, area):
            if x >= 0 and x < len(section) and y >= 0 and y < len(section[0]) and section[x][y]:
                section[x][y] = 0
                
                if not border(section, x, y):
                    area.append((x, y))
                
                for p, q in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    flood(section, x + p, y + q, area)
        
        def find_island(island, dq):
            for i in range(len(islands)):
                for k in range(len(islands[0])):
                    if islands[i][k] == 1:
                        flood(islands, i, k, dq)
                        return dq
            
        islands = A[:]
        visited = set()
        output = float("inf")                    
        count = 0
        island1 = find_island(islands, deque())
        
        while island1:
            level = deque()
            
            while island1:
                pos = island1.popleft()
                
                if (
                    pos in visited 
                    or pos[0] < 0 
                    or pos[0] >= len(islands) 
                    or pos[1] < 0 
                    or pos[1] >= len(islands[0])
                   ):
                    continue
                if islands[pos[0]][pos[1]]:
                    return count - 1
                visited.add(pos)
                
                for p, q in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    level.append((p + pos[0], q + pos[1]))
            
            count += 1
            island1 = level
