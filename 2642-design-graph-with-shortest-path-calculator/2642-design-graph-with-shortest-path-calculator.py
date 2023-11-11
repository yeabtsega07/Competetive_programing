class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = defaultdict(list)
        
        for edge in edges:
            self.graph[edge[0]].append((edge[1], edge[2]))

    def addEdge(self, edge: List[int]) -> None:
        
        self.graph[edge[0]].append((edge[1], edge[2]))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        
        heap = [(0, node1)]
        cost = [float("inf")] * self.n
        cost[node1] = 0
        # visited = set([(node1, 0)])
        
        while heap:
            
            cur_cost , cur_node = heappop(heap)
            
            if cur_cost > cost[cur_node]:
                continue
            
            if cur_node == node2:
                self.graph[node1].append((node2, cur_cost))
                return cur_cost
            
            for child, child_cost in self.graph[cur_node]:
                
                new_cost = child_cost + cur_cost
                
                if new_cost < cost[child]:
                    cost[child] = new_cost
                    heappush(heap, (new_cost, child))
                    # visited.add((child, new_cost))
            
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)