class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        ArrayList[] graph = new ArrayList[numCourses];
        boolean[] visited = new boolean[numCourses];
        boolean[] noCycle = new boolean[numCourses];
        
        for (int i = 0; i < numCourses; i++) {
            graph[i] = new ArrayList();
        }
        
        for (int j = 0; j < prerequisites.length; j++) {
            graph[prerequisites[j][1]].add(prerequisites[j][0]);
        }
        
        for(int k = 0; k < numCourses; k++) {
            if (dfs(graph, visited, noCycle, k) == false) {
                return false;
            }
        }
        
        return true;
    }
    
    public boolean dfs(ArrayList[] graph, boolean[] visited, boolean[] noCycle, int course) {
        if (visited[course]) {
            return false;
        } else if (noCycle[course]){
            return true;   
        } else {
            visited[course] = true;
        }
        for (int i = 0; i < graph[course].size(); i++) {
            int target = (int)graph[course].get(i);
            if (visited[target]) {
                return false;
            } else {
                dfs(graph, visited, noCycle, target);
            }
        }
        visited[course] = false;
        noCycle[course] = true;
        return true;
    }
}
