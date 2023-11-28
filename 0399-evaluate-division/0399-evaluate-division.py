class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        
        for i, val in enumerate(equations):
            
            graph[val[0]].append((val[1], values[i]))
            graph[val[1]].append((val[0], 1 / values[i]))
        
        def bfs(start, end):
            
            if end not in graph.keys() or start not in graph.keys():
                return -1.00
            
            queue = deque([(start, 1)])
            visited = set([start])
            
            while queue:
                
                cur, val = queue.popleft()  
                
                if cur == end:
                    return val
                
                for child in graph[cur]:
                    
                    if child[0] not in visited:
                        
                        queue.append((child[0], val * child[1]))
                        visited.add(child[0])
            
            return -1.00
        
        result = []
        
        for query in queries:
            
            val = bfs(query[0], query[1])
            result.append(val)
        
        return result