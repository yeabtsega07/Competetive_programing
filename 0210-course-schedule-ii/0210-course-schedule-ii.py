class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        result = []
        color = [0] * numCourses
        stack, visited = [], set()
        inDegree = [0] * numCourses
        
        
        for end, start  in prerequisites:
            graph[start].append(end)
            inDegree[end] += 1
            
        start = []
        for index , val in enumerate(inDegree):
            
            if not val:
                start.append(index)
        
        
        def dfs( node ):

            if color[node] == 1:
                return True
            
            if color[node] == 2:
                return False


            color[node] = 1
            for child in graph[node]:

                if dfs(child):
                    return True
                        

            stack.append(node)
            color[node] = 2
            
            return False            
        
        for val in start:
            
            if dfs( val ):
                return []
    
        return stack[::-1] if len(stack) == numCourses else []
                
                
        