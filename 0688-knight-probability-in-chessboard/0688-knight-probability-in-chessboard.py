class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float: 
        
        if k == 0:
            return 1
        
        
        def inBound ( x, y, n = n ):
            
            return 0 <= x <= n - 1 and 0 <= y <= n - 1
        
        dp = {}        
        moves = [(1,2), (2, 1), (-1,2), (1,-2), (-1, -2), (2, -1), (-2, -1), (-2, 1) ]        

        def recur ( row, col, cnt, k ):
            
            if not inBound(row, col ):
                return 0
            
            if cnt == k and inBound(row, col):
                return 1
            
            if (row, col, cnt) in dp:
                return dp[(row, col, cnt)]
            
            cur = 0
            for move in moves:
                
                cur += recur( row + move[0], col + move[1], cnt + 1, k) / 8
            
            dp[(row, col, cnt)] = cur
            
            return cur
        
        return recur( row, column, 0, k)
       