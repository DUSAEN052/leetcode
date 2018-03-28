class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """        
        def findPath(graph, curr, path, output):
            np = [] + path
            np.append(curr)
            
            if not graph[curr]:
                output.append(np[:])
            
            for nums in graph[curr]:
                findPath(graph, nums, np, output)
        
        output = []
        findPath(graph, 0, [], output)
        
        return output
