class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        #base case 
        if source == target:
            return 0
        
        routes = [ set(route) for route in routes]
        queue = deque()
        graph = defaultdict(list)
        for i in range(len(routes)):
            if source in routes[i]:
                queue.append([i,1])
                
            for j in range(len(routes)):
                if i != j:
                    for val in routes[i]:
                        if val in routes[j]:
                            graph[i].append(j)
                            break
        # print(1)
        visited = set()
        track = []
        while queue:
            
            node, count = queue.popleft()
            if target in routes[node]:
                track.append(count)
            
            for child in graph[node]:
                
                if child not in visited:
                    visited.add(child)
                    queue.append([child, count + 1])
        
        # print(track)
        # # print(1)
        return min(track) if track else -1