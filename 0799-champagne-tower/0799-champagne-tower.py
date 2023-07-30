class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        track = defaultdict(int)
        track[(0,0)] = poured
        
        for row in range(100 + 1):
            for glass in range(row + 1):
                
                if track[(row, glass)] >= 1:
                    track[(row + 1, glass)] += (track[(row, glass)] - 1) / 2
                    track[(row + 1, glass + 1)] += (track[(row, glass)] - 1) / 2
                    track[(row, glass)] = 1
        
        return track[(query_row, query_glass)]
            
            
            
            