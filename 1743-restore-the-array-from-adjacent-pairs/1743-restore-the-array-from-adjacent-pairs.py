class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        n = len(adjacentPairs)
        graph = defaultdict(list)
        result = []
        color = defaultdict(int)
        stack, visited = [], set()
        inDegree = defaultdict(int)
        
         
        for start, end  in adjacentPairs:
            graph[start].append(end)
            graph[end].append(start)
            inDegree[end] += 1
            inDegree[start] += 1
            
        start = []
    
        for index , val in inDegree.items():
            
            if val == 1:
                start.append(index)
                
        def dfs ( node, result ):
            stack = [node]
            visited.add(node)
            
            while stack:
                
                node = stack.pop()
                result.append(node)

                for child in graph[node]:
                    
                    if child not in visited:
                        visited.add(child)
                        stack.append(child)
            return result
                        
            
        
                
        result = []
        for node in start:
            
            if node not in visited:
                check = dfs(node, [])
                result += check
        
        return result