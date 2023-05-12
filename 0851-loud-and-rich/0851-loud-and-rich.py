class Solution:
    def loudAndRich(self, edges: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        track = defaultdict(set)
        graph = defaultdict(list)
        inDegrees = [0] * n
        
        for edge in edges:
            
            graph[edge[0]].append(edge[1])
            inDegrees[edge[1]] += 1
        
        for i in range(n):
            track[i].add(i)
        
        queue = deque()
        for index, inDegree in enumerate( inDegrees ):
            
            if not inDegree:
                queue.append([index, -1])

        while queue:
            
            node, parentNode = queue.popleft()
            if parentNode >= 0:
                track[node].update(track[parentNode])
                track[node].add(parentNode)
            
            for child in graph[node]:
                
                inDegrees[child] -= 1 
                track[child].update(track[node])
                track[child].add(node)
                if not inDegrees[child]:
                    queue.append([child, node])
        
        result = []
        # print(track)
        for i in range(n):
            
            if track[i]:
                result.append( min(track[i], key = lambda x:quiet[x]))
            else:
                result.append(i)
        return result
                