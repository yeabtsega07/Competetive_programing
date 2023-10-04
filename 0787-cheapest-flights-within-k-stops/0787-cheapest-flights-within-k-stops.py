class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))
        
        visited = set([src, 0])
        heap = [(0, src, 0)]
        
        
        while heap:
            
            # print(heap, "this")
            cur_val, cur_node, cur_t = heappop(heap)
            
            # print(cur_val, cur_node, cur_t)
            if cur_node == dst and cur_t - 1 <= k:
                return cur_val
            
            for child_node, child_val in graph[cur_node]:
                
                if cur_t - 1 < k and (child_node, cur_val + child_val) not in visited:
                    heappush(heap, (cur_val + child_val, child_node, cur_t + 1))
                    visited.add((child_node, cur_val + child_val))

        
        return -1 