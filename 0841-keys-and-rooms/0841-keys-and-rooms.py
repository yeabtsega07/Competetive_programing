class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        

        def depth_first_search(rooms: list[list[int]]) -> bool:
            n = len(rooms)

            visited = [False] * n

            def dfs(u: int):
                visited[u] = True

                for v in rooms[u]:
                    if not visited[v]:
                        dfs(v)

            dfs(0)

            return all(visited)
        return depth_first_search(rooms)
        
        