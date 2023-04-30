class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        check = set(deadends)
        
        def bfs(check, target, node):
            
            def getChilds( wheel ):
                
                childs = []
                
                for i,lock in enumerate(wheel):
                    
                    if wheel[i] > 0:
                        wheel[i] -= 1
                        childs.append(wheel[:])
                        wheel[i] += 1
                    else:
                        wheel[i] = 9
                        childs.append(wheel[:])
                        wheel[i] = 0
                    
                    if wheel[i] < 9:
                        wheel[i] += 1
                        childs.append(wheel[:])
                        wheel[i] -= 1
                    else:
                        wheel[i] = 0
                        childs.append(wheel[:])
                        wheel[i] = 9
                
                return childs
                            
            
            visited = set([tuple(node)])
            queue = deque([[node, 0]])
            
            while queue:
                
                node, count = queue.popleft()
                
                if "".join(map(str,node)) in check:
                    return -1
                
                if "".join(map(str,node)) == target:
                    return count
                
                for child in getChilds ( node ):
                    print(child if child[0] == 8 else -1)
                    if tuple(child) not in visited and "".join(map(str,child)) not in check:
                        
                        visited.add( tuple(child) )
                        queue.append( [child, count + 1] )
            
            return -1
        
        return bfs( check, target, [0,0,0,0])
                        
                        
                        
                        
                        
                        
                        