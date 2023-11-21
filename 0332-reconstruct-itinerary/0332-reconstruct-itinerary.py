class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)

        
        for ticket in tickets:
            
            graph[ticket[0]].append(ticket[1])

        
        for key in graph:
            graph[key] = sorted(graph[key], reverse = True)
        
        route = []
        def dfs( city ):
            while graph[city]:
                dfs(graph[city].pop())
            
            route.append(city)
        
        dfs("JFK")
        
        return route[::-1]
        

                
                
                
                
            