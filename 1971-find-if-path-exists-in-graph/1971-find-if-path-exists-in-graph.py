class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        q = deque(edges)
        src = {source}
        des = {destination}
        
        while q:
            lth = len(q)
            for _ in range(lth):
                a,b = q.popleft()
                if (a in src or b in src) and (a in des or b in des):
                    return True
                elif a in src or b in src:
                    src.update({a,b})
                elif a in des or b in des:
                    des.update({a,b})
                else:
                    q.append([a,b])
            if len(q) == lth:
                return False
        