class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n, m = len(matrix), len(matrix[0])
        i, j = n - 1, 0
        
        # x, y = i, j
        # track = {}
        while i >= 0:
            x, y = i, j
            pre = -1
            while x < n and y < m:
                # print(x,y)
                if pre > -1:
                    if pre  != matrix[x][y]:
                        
                        return False
                else:
                    pre = matrix[x][y]
                x += 1
                y += 1
            i -= 1    
        # print(i,j,"alsdbnl")
        i = 0
        while j < m:
            
            x, y = i, j
            pre = -1
            while x < n and y < m:
                # print(x,y)
                if pre > -1:
                    if pre  != matrix[x][y]:
                       
                        return False
                else:
                    pre = matrix[x][y]
                x += 1
                y += 1
            
            j += 1
        return True     
            
            
                
            
            
            
                
        