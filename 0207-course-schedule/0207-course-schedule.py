class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
            
            cur = queue.pop()
            result.append(cur)
            for child in graph[cur]:
                
                inDegree[child] -= 1
                if not inDegree[child]:
                    queue.append(child)
                    visited.add(child)
        
        return True if len(result) == numCourses else False
        
        