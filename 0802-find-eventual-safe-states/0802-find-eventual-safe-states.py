class Solution:
    def eventualSafeNodes(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for i ,edge in enumerate(edges):
            
            graph[i] += edge
        
        visited = [0] * len(edges)
        stack = []
        def dfs ( node ):
            
            if visited[node] == 2:
                return False
            
            if visited[node] == 1:
                return True
            
            visited[node] = 1
            
            for child in graph[node]:
                
                if dfs( child ):
                    return True
            
            visited[node] = 2
            stack.append(node)
            return False
        
        for i in range( len(edges) ):
            
            if not visited[i]:
                dfs(i)
        
        return sorted(stack)
                
        