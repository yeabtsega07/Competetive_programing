class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            
        def bfs(start, end):
            queue = deque([(start,[start])])
            visited = set([start])
            
            while queue:
                
                cur = queue.popleft()
                
                if cur[0] == end:
                    return cur[1]
        
                for child in graph[cur[0]]:
                    if child not in visited:
                        visited.add(child)
                        queue.append((child,cur[1] + [child]))
            return cur[1]           
        
        count = defaultdict(int)
        for start, end in trips:
            path = bfs(start, end)
            for node in path:
                count[node] += 1
        
        dp = {}
        def recur(cur, pre, check):
            
            # print(dp)
            if (cur, pre, check) in dp:
                return dp[(cur, pre, check)]
            
            if check:
                cost = count[cur] * (price[cur] // 2)
            else:
                cost = count[cur] * price[cur]
                
            half, notHalf = float("inf") ,float("inf") 
            for child in graph[cur]:
                if child != pre :
                    if check:
                        half = recur(child, cur, False)
                    else:
                        notHalf = min(recur(child, cur, True), recur(child, cur, False))
                        
                    cost += min(half, notHalf)
                    
            dp[(cur, pre, check)] = cost
            return dp[(cur, pre, check)]
        
        res = float("inf")
        for node in range(n):
            res = min(recur(node, None, True), recur(node, None, False))
        
        return res
                    