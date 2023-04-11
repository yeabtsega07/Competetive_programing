class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visited = set()
        
        def dfs ( node, visited ):
            
            visited.add(node)
            
            for child in graph[node]:
                
                if child not in visited:
                    dfs(child, visited)
        
        result = 0
        
        for key in graph.keys():
            
            if key not in visited:
                dfs(key, visited)
                result += 1
        
        return result
                