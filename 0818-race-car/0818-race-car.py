class Solution:
    def racecar(self, target: int) -> int:
        
        
        def bfs( pos, speed, target ):
            
            def getChild( pos, speed ):
                
                child  = []
                child.append((pos + speed, speed * 2))
                if speed >= 0:
                    child.append((pos, -1))
                else:
                    child.append((pos, 1))
                
                return child
            
            visited = set([(pos, speed)])
            queue = deque([(pos, speed, 0)])
            
            while queue:
                
                pos, speed, count = queue.popleft()
                
                if pos == target:
                    
                    return count
                
                for child in getChild(pos, speed):
                    
                    if child not in visited:
                        
                        visited.add(child)
                        queue.append((child[0],child[1], count + 1))
            
            return 0
        
        return bfs( 0, 1, target )
        