class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        ans = [0] * n
        visited = [0] * n

        def dfs(node):
            if visited[node]:
                return {}
            visited[node] = 1

            cnt = {labels[node]: 1}
            for child in graph[node]:
                cnt = dict(Counter(cnt) + Counter(dfs(child)))

            ans[node] = cnt[labels[node]]

            return cnt

        dfs(0)
        return ans