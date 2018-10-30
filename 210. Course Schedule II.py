from collections import defaultdict
class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        tree = defaultdict(list)
        degree = [0] * numCourses
        output = []
        
        for p in prerequisites:
            tree[p[1]].append(p[0])
            degree[p[0]] += 1
        
        q = [i for i in range(numCourses) if degree[i] == 0]
        
        while q:
            node = q.pop(0)
            output.append(node)
            
            for child in tree[node]:
                degree[child] -= 1
                
                if degree[child] == 0:
                    q.append(child)
        
        return output if len(output) == numCourses else []
