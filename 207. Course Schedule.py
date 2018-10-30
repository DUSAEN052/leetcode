from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        tree = defaultdict(list)
        degree = [0] * numCourses
        visited = 0
        
        for p in prerequisites:
            tree[p[1]].append(p[0])
            degree[p[0]] += 1
        
        q = [i for i in range(numCourses) if degree[i] == 0]
        
        while q:
            node = q.pop(0)
            visited += 1
            
            for child in tree[node]:
                degree[child] -= 1
                
                if degree[child] == 0:
                    q.append(child)
        
        return visited == numCourses
