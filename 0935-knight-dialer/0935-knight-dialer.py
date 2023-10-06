class Solution:
    def knightDialer(self, n: int) -> int:
        
        numPad = [["1","2","3"], ["4","5","6"], ["7","8","9"], ["*","0","#"]]
        
        
        def inBound(row, col):
            return 0 <= row < 4 and 0 <= col < 3
        
        dir  =  [(2,1), (2,-1), (1, 2), (-1, 2), (-2, -1), (-2, 1), (-1, -2), (1, -2)]
        @cache
        def recur( row, col, count):
            
            if not inBound(row, col) or (row, col) == (3, 0) or (row, col) == (3, 2) :
                return 0
            
            if count == n:
                return 1
            
            track = 0
            for c_row, c_col in dir:
                new_row = row + c_row
                new_col = col + c_col
                
                cur = recur(new_row, new_col, count + 1)
                track += cur
            
            return track
        
        res = 0
        for i in range(4):
            for j in range(3):
                res += recur(i, j, 1)
        # print(res)
        return res % (10**9 + 7) 
                
                
                
        