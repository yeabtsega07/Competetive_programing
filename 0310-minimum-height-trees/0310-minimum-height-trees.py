class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        inDegree = [0] * (n)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

            inDegree[u] += 1
            inDegree[v] += 1

        queue = deque()   
        for i in range(n):
            if inDegree[i] == 1:
                queue.append(i) 
                
        # print(inDegree, queue)
        res = []
        while queue:

            lenght = len(queue)
            if queue:
                res = list(queue)
            for i in range(lenght):

                node = queue.popleft()
                inDegree[node] -= 1

                for neighbor in graph[node]:

                    inDegree[neighbor] -= 1

                    if inDegree[neighbor] == 1:

                        queue.append(neighbor)   


        return res if edges else [0]
        