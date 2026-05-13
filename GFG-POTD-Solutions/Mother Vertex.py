class Solution:
    def findMotherVertex(self, V, edges):
        adj = [[] for _ in range(V)]
        
        for u, v in edges:
            adj[u].append(v)
        
        visited = [False] * V
        
        def dfs(node):
            visited[node] = True
            
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)
        
        candidate = -1
        
        for i in range(V):
            if not visited[i]:
                dfs(i)
                candidate = i
        
        visited = [False] * V
        dfs(candidate)
        
        for i in range(V):
            if not visited[i]:
                return -1
        
        return candidate