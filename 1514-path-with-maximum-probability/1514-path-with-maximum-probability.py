class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        
        graph = defaultdict(list)
        for i, edge in enumerate(edges):
            graph[edge[0]].append((edge[1], succProb[i]))
            graph[edge[1]].append((edge[0], succProb[i]))
        
        
        
        heap = [(1, start_node )]
        visited = set()
        
        
        while heap:
            
            prob, node = heappop(heap)
            
            if node in visited:
                continue
            
            visited.add(node)
            
            if node == end_node:
                return abs(prob)
            
            for child, c_prob in graph[node]:
                dist = (abs(prob) * c_prob)
                heappush(heap, ( -dist , child))

        
            
        return 0.000000