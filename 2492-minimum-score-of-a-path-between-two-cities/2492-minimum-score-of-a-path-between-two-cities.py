class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for i, j, dis in roads:
            
            graph[i].append((j,dis))
            graph[j].append((i,dis))

        queue = deque([1])
        visited, result = set(), float("inf")
        while queue:
            
            node = queue.popleft()

            for child in graph[node]:
                
                result = min(result, child[1])
                
                if child[0] not in visited:
                    visited.add(child[0])
                    queue.append(child[0])
        
        return result
                
                
                
                