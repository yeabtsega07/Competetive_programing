class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for i, j, dis in roads:
            
            graph[i].append([j,dis])
            graph[j].append([i,dis])

        visited, result = set(), [float("inf")]    
        def dfs( node ): 
            
            visited.add(node)
            
            for child in graph[node]:
                
                result[0] = min( child[1], result[0] )
                
                if child[0] not in visited:
                    
                    dfs( child[0] )
        
        dfs(1)
        
        return result[0]
                
                