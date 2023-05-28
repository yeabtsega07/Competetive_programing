class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for point in points:
            for point1 in points:
                if point1 != point:
                    dis = abs(point[0]-point1[0]) + abs(point[1]-point1[1])
                    graph[tuple(point)].append([dis,point1[0],point1[1]])
        
        visited = set([tuple(points[0])])
        heap = []
        queue = deque([[0,points[0][0],points[0][1]]])
        res = 0
        
        while queue:
            
            cur = queue.popleft()
            res += cur[0]
            
            for val in graph[(cur[1],cur[2])]:
                
                if (val[1],val[2]) not in visited:
                    heappush(heap,val)
            
            check = None
            if heap:
                check = heappop(heap)
            while check and  (check[1],check[2]) in visited and heap:
                check = heappop(heap)
                
            if check and (check[1],check[2]) not in visited:
                queue.append(check)
                visited.add((check[1],check[2]))
        
        return res
                
                
                
                
                
            