from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def dfs(tree, root, target, visited):
            visited.add(root)
            
            if root == target and len(visited) >= 3:
                return True

            for child in tree[root]:
                visit = set(visited)
                
                if child not in visit:
                    if dfs(tree, child, target, visit):
                        return True
            return False
                
        tree = defaultdict(set)
        
        for edge in edges:
            tree[edge[0]].add(edge[1])
            tree[edge[1]].add(edge[0])
        
        for i in range(len(edges) -1, -1, -1):
            if dfs(tree, edges[i][0], edges[i][1], set()):
                return [edges[i][0], edges[i][1]]
