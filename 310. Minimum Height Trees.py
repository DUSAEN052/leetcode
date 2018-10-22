from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return [0]
        
        tree = defaultdict(set)
        degree = [0] * n
        
        for edge in edges:
            tree[edge[0]].add(edge[1])
            tree[edge[1]].add(edge[0])
            degree[edge[0]] += 1
            degree[edge[1]] += 1
       
        q = [i for i in range(n) if degree[i] == 1]
        
        while q:
            tmp = []
            
            for node in q:
                for t in tree[node]:
                    degree[t] -= 1
                    if degree[t] == 1:
                        tmp.append(t)
            
            if not tmp:
                return q
            q = tmp
