class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        inDegree = [0] * numCourses
        check = [[] for _ in range(numCourses)]
        queue = deque()
        
        for start, end  in prerequisites:
            graph[start].add(end)
            inDegree[end] += 1
        
        for index , val in enumerate(inDegree):
            
            if not val:
                queue.append(index)

        result = []
        while queue:
            
            cur = queue.pop()

            for child in graph[cur]:
                for val in check[cur]:
                    if val not in check[child]:
                        check[child].append(val)
                
                check[child].append(cur)
                inDegree[child] -= 1
                if not inDegree[child]:
                    queue.append(child)


        for query in queries:
            
            if query[0] in check[query[1]]:
                result.append(True)
            else:
                result.append(False)
        
        return result
        
        