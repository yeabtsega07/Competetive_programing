class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[[], []] for _ in range(n)]  
        
        for a, b in redEdges:
            graph[a][0].append(b)
        for a, b in blueEdges:
            graph[a][1].append(b)
        

        queue = deque([(0, 0), (0, 1)])
        visited = set([(0, 0), (0, 1)])
        answer = [-1 for _ in range(n)]

        dist = 0
        while queue:
            for _ in range(len(queue)):
                node, color = queue.popleft()
                if answer[node] == -1:
                    answer[node] = dist
                alternative = 1 - color

                for neighbour in graph[node][alternative]:
                    if (neighbour, alternative) not in visited:
                        visited.add((neighbour, alternative))
                        queue.append((neighbour, alternative))
            dist += 1
            
        return answer