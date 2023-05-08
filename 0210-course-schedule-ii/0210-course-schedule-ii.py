class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        inDegree = [0] * numCourses
        queue = deque()
        
        for end, start  in prerequisites:
            graph[start].append(end)
            inDegree[end] += 1
        
        for index , val in enumerate(inDegree):
            
            if not val:
                queue.append(index)
        
        visited = set()
        result = []
        while queue:
            
            cur = queue.popleft()
            result.append(cur)
            for child in graph[cur]:
                
                inDegree[child] -= 1
                if not inDegree[child]:
                    queue.append(child)
                    visited.add(child)
        
        return result if len(result) == numCourses else []
                    
        