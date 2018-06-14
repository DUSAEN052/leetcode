class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        
        def visit(key, rooms):
            if rooms[key] and key not in visited:
                visited.add(key)
                
                for k in rooms[key]:
                    visit(k, rooms)
            
            elif not rooms[key]:
                visited.add(key)
        
        visit(0, rooms)
        
        return len(visited) == len(rooms)
