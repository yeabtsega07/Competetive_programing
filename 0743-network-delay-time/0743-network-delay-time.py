class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[1], time[2]))
        
        
        distances = {i : float("inf") for i in range(1, n + 1)}
        distances[k] = 0
        
        visited = set()
        heap = [(0, k)]
        
        while heap:
            
            cur_val, cur_node = heappop(heap)
            
            if cur_node in visited:
                continue
            
            visited.add(cur_node)
            
            for child_node, val in graph[cur_node]:
                
                cur_dist = val + cur_val
                
                if cur_dist < distances[child_node]:
                    distances[child_node] = cur_dist
                    heappush(heap, (cur_dist, child_node))
        
        res = max(distances.values())
        return res if res != float("inf") else -1