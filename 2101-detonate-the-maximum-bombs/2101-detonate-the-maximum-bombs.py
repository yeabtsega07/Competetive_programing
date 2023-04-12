class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for i , bomb in enumerate(bombs):
            
            for j, check in enumerate(bombs):
                
                if i != j and sqrt((bomb[0] - check[0]) ** 2 + (bomb[1] - check[1]) ** 2 ) <= bomb[-1]:
                    
                    graph[i].append(j)
        
        if not graph:
            return 1
        
        result = 0
        
        
        def dfs ( node, visited ):
            
            visited.add(node)
            count.append(1)

            for child in graph[node]:

                if child not in visited:
                    dfs( child, visited )
        
        # print(graph)
        for i, bomb in enumerate(bombs):
            
            count = []
            visited = set()
            dfs(i, visited)
            result = max(result, sum(count))
        
        return result
            
                    